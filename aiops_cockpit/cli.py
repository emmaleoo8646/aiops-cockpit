import argparse

from aiops_cockpit import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aiops-cockpit",
        description="AI 运维驾驶舱 — 监控、分析并修复企业信息系统问题",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("serve", help="启动本地 Web 服务（计划在 P2 实现）")
    sub.add_parser("collect", help="执行一轮目标系统采集（计划在 P1/P4 实现）")
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    if args.command == "serve":
        print("[P0] serve 命令尚未实现，将在 P2 实现")
        return 0
    if args.command == "collect":
        print("[P0] collect 命令尚未实现，将在 P1/P4 实现")
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
