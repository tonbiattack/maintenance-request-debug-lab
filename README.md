# Maintenance Request Debug Lab

設備点検・保全依頼を題材にした、BFF・Redis・外部APIを使わないデバッグ教材です。Vue画面、Flask API、PostgreSQLの3層を対象に、HTTP契約、画面状態、SQL、Transaction、DB制約、Kubernetes設定を観測します。

| コマンド | 用途 |
| --- | --- |
| `pnpm install` | Vue側の依存関係を導入する。 |
| `./scripts/verify.sh` | TypeScript、Python、文書、差分を検証する。 |
| `docker compose up --build` | Web、API、PostgreSQLを起動する。 |

`docs/issues/`から一問を選び、バグ導入コミットに切り替えて調査してください。解答は自分の修正と回帰テストを作った後に開きます。
