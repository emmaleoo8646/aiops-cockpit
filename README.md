# AIOps Cockpit

AI 运维驾驶舱 — 独立部署、低侵入的 Windows 智能体，自动采集、分析、展示企业信息系统的**安全、业务、系统**三类问题，并对每个问题给出根因与改进建议。

## 当前状态

| 阶段 | 内容 | 状态 |
|---|---|---|
| P0 | 仓库脚手架 + 打包流水线 + CI | 进行中 |
| P1 | 采集框架（WinRM / SSH / WMI / SNMP / HTTP / DB） | 待开始 |
| P2 | 存储层 + 驾驶舱骨架 | 待开始 |
| P3 | AI 引擎（云端 LLM） | 待开始 |
| P4 | 三域采集实现 | 待开始 |
| P5 | 打包 + Windows 服务化 | 待开始 |
| P6 | 知识库 + 文档 | 待开始 |

设计稿：`docs/design.md`（已确认关键决策，AI 推理采用云端 LLM）

## 安装（开发模式）

```bash
pip install -e ".[dev]"
```

## 运行测试

```bash
pytest
```

## CLI 入口

```bash
aiops-cockpit --help
python -m aiops_cockpit --help
```

## 仓库约定

- 每次改动 = 1 个 commit
- 每次改动必须有相关测试
- 交付前所有测试必须通过
- 详见 `AGENTS.md`

## 许可证

MIT
