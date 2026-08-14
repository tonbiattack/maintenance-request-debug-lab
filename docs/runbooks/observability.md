# 観測ランブック

最初にBrowserのNetworkでリクエスト、HTTPステータス、`X-Request-Id`、応答本文を確認します。次にFlaskの構造化ログで同じIDを検索し、リクエスト入力、SQL実行、Transaction完了、応答を照合します。

一覧問題ではSQLの`ORDER BY`、limit、offset、発行数を確認します。更新問題ではversion、更新件数、状態・履歴の両方のDB状態、migrationの制約を確認します。Kubernetes問題ではPodイベント、ConfigMap、環境変数、probe応答を確認します。
