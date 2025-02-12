# -*- coding: utf-8 -*-
import asyncio
import sys
from asyncio.subprocess import PIPE

# 設置默認編碼為 UTF-8
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

JUDGE_PREFIX = "[JUDGE] "
SOLVER_PREFIX = "[SOLVE] "

async def pipe_data(name: str, reader: asyncio.StreamReader, writers: list, stdout=None, prefix=""):
    """處理進程間的數據傳輸"""
    try:
        while True:
            data = await reader.readline()
            if not data:
                break
                
            # 寫入到其他進程
            for writer in writers:
                if isinstance(writer, asyncio.StreamWriter) and not writer.is_closing():
                    writer.write(data)
                    await writer.drain()
            
            # 輸出到終端
            if stdout:
                stdout.buffer.write(prefix.encode('utf-8') + data)
                stdout.flush()
    except Exception as e:
        print(f"Pipe error {name}: {e}", file=sys.stderr)

async def async_main():
    # 設置 Windows 的事件循環策略
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    # 啟動進程
    judge = await asyncio.create_subprocess_exec(
        sys.executable, 'judge.py',
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )
    
    solver = await asyncio.create_subprocess_exec(
        sys.executable, 'solve.py',
        stdin=PIPE, stdout=PIPE, stderr=PIPE
    )

    try:
        # 設置通信管道
        await asyncio.gather(
            pipe_data('judge', judge.stdout, [solver.stdin], sys.stdout, JUDGE_PREFIX),
            pipe_data('solver', solver.stdout, [judge.stdin], sys.stdout, SOLVER_PREFIX),
            pipe_data('judge_err', judge.stderr, [], sys.stderr, JUDGE_PREFIX),
            pipe_data('solver_err', solver.stderr, [], sys.stderr, SOLVER_PREFIX)
        )
    finally:
        # 確保進程結束
        for proc in [judge, solver]:
            if proc and proc.returncode is None:
                try:
                    proc.terminate()
                    await proc.wait()
                except Exception as e:
                    print(f"Process termination error: {e}", file=sys.stderr)

def main():
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user", file=sys.stderr)

if __name__ == "__main__":
    main()