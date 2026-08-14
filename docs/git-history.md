# Git履歴の対応

受講者はバグ導入コミットに切り替え、Issueだけを根拠に再現・観測・最小修正・回帰テスト追加を行います。その後、修正コミットと`solutions/`を比較してください。`master`はすべての修正を含み、全テストが成功する状態です。

| ID | バグ導入コミット | 修正コミット | 比較の主対象 |
| --- | --- | --- | --- |
| M01 | `0a751c5` | `f30c28f` | Flask検証エラーのHTTPステータス |
| M02 | `88a62db` | `cda9458` | 状態・ページごとのQuery cache key |
| M03 | `6e3b11b` | `12ca1b4` | 一覧の安定したSQL順序 |
| M04 | `877bcec` | `aba1ca5` | 担当割当の競合検知 |
| M05 | `fce1038` | `d7e3fbd` | 期限時刻のUTC正規化 |
| M06 | `025aec8` | `5059bf1` | 担当者一覧の一括クエリ |
| M07 | `253f509` | `13cdd46` | 完了処理の原子性 |
| M08 | `42c022e` | `ca9df49` | 状態値のDB制約契約 |
| M09 | `9758306` | `36aef8e` | 担当者表示名の必須契約 |
| M10 | `04c9836` | `8d342f1` | APIのrequestId記録 |
| M11 | `5f64ca1` | `f53b8fb` | KubernetesのDBホスト名 |
| M12 | `5b88d03` | `d56be2f` | 完了フォームの依頼ID同期 |

たとえばM03は次のように始めます。

```bash
git checkout 6e3b11b
# Issueを読み、同一ページのHTTP応答とSQL順序を繰り返し比較する
git diff 6e3b11b 12ca1b4 -- api/app/service.py
git checkout master
```
