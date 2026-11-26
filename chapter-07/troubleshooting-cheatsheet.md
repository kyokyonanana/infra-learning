# Docker トラブルシューティング早見表

## 調査の流れ
1. docker ps -a
2. docker logs
3. docker inspect (State.ExitCode / OOMKilled)
4. docker events
5. docker exec / --pid container:NAME で相乗り

## 終了コード
- 137: SIGKILL (OOMKilled か docker kill)
- 143: SIGTERM
- 127: command not found
- 126: permission denied

## セキュリティ
- 非root / --read-only / --cap-drop ALL / no-new-privileges
- docker.sock、--privileged は渡さない
