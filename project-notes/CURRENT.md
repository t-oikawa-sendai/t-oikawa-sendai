# CURRENT（現在地点）

<details>
<summary>Document Info（文書情報）｜PROFILE-CURRENT-001｜0.13｜Draft</summary>

| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | PROFILE-CURRENT-001 |
| Version（バージョン） | 0.13 |
| Status（ステータス） | Draft |
| Created Date（作成日） | 2026-10-18 |
| Last Updated（最終更新日） | 2026-10-23 |
| Owner（管理者） | Takashi Oikawa |
| Related Documents（関連文書） | ../README.md / ../CONSTITUTION.md / ../AGENTS.md |

</details>

## Purpose（目的）

GitHubプロフィールを生徒向け教材の総合入口とし、教材概要・リンク・公開区分・直近5件の更新履歴を案内する。

## Completed（完了）

- 2026-10-18：READMEに公開Repository 8件を掲載しmainへ反映（da53969）。
- 2026-10-18：LEARNING標準の3文書を導入し、3件のリンクに印を付けてmainへ反映（b843382）。
- 2026-10-20：削除予定Repositoryへのリンクを削除してmainへ反映（9837c7d）。
- 2026-10-23：READMEとCURRENTの整備をmainへ反映（fbdc818）。プロフィールRepositoryのPublic・default branch mainと、公開プロフィールOverviewでのREADME「教材案内」表示を確認。ローカルcloneの存在とmainのorigin/mainへの同期を確認。
- 2026-10-23：プロフィールREADMEのデザイン案とバナー画像をプレビュー用ブランチ `preview/profile-readme-design-20261023` に配置。ブラウザでREADMEの表示を確認。mainへの反映は未実施。
- 2026-10-23：プレビュー用READMEの上下181pxのSVG装飾帯を作成してブランチへ反映（40fb27f）。GitHubのブラウザで上部・下部の実表示を確認。mainへの反映は未実施。
- 2026-10-23：プレビュー用READMEの公開範囲とログイン・404案内の文言を修正してブランチへ反映（36ccc61）。GitHubのブラウザで新文言の表示、旧説明の削除、上下バナーの残存を確認。mainへの反映は未実施。
- 2026-10-23：上下181pxのバナーをエンジ系に再配色し、上部中央に「教材案内」を配置してプレビュー用ブランチへ反映（53f28f1）。SVG構文・描画・差分と、GitHubブラウザでのタイトル・上下バナー表示を確認。mainへの反映は未実施。
- 2026-10-23：利用者指定順の5教材一覧をプレビュー用ブランチへ反映（b7102b2）。GitHubブラウザで指定順、Officeデモ除外、設計文書管理入門のリンクなし、JEV・score-readerのリンク、上下バナーと公開範囲案内を確認。mainへの反映は未実施。

## Current（現在）

- プロフィールRepositoryはPublic、default branchはmain。公開プロフィールOverviewにREADME「教材案内」が表示されている。
- 受講生用AI教材は前回の接続では取得できず、Visibility・更新内容・受講生権限は未確認。
- READMEは公開方針と実状態を区別し、講師用正本への生徒向けリンクを掲載していない。更新履歴5件を手動で管理している。
- エンジ系と上部タイトルを合わせた案はプレビュー用ブランチで表示確認済み。公開プロフィールOverviewのmainには未反映。
- プレビュー用READMEの案内文は利用者指定の文言でGitHub表示確認済み。
- 5教材の一覧改訂案はプレビュー用ブランチで表示確認済み。公開プロフィールOverviewのmainには未反映。設計文書管理入門の受講生向け配布Repositoryは未作成。

## Next（次）

- 受講生用教材のVisibility・権限と公開可能な更新内容を確認する。
- Visibility変更は未承認のため実施しない。
- プレビュー用ブランチのデザインの採用を判断する。

## Blockers（阻害要因）

- 受講生用RepositoryのVisibility・権限等は未確認。
- 設計文書管理入門の受講生向け配布Repositoryは未作成。

## Related Decisions（関連Decision）

- なし。2026-10-23の利用者提示「GitHubプロフィール・教材案内ページ整備指示」を今回仕様の根拠とする。
