# CURRENT（現在地点）

<details>
<summary>Document Info（文書情報）｜PROFILE-CURRENT-001｜0.6｜Draft</summary>

| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | PROFILE-CURRENT-001 |
| Version（バージョン） | 0.6 |
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
- 2026-10-23：プロフィールREADMEのデザイン案とバナー画像をプレビュー用ブランチ `preview/profile-readme-design-20261023` に配置。ブラウザでの表示確認とmainへの反映は未実施。

## Current（現在）

- プロフィールRepositoryはPublic、default branchはmain。公開プロフィールOverviewにREADME「教材案内」が表示されている。
- 前回確認時、dokoTsubu-platformはPublic。office-addin-dokotsubu-demoは限定公開方針に対しPublic。
- 受講生用AI教材は前回の接続では取得できず、Visibility・更新内容・受講生権限は未確認。
- READMEは公開方針と実状態を区別し、講師用正本への生徒向けリンクを掲載していない。更新履歴5件を手動で管理している。
- プレビュー用ブランチにはデザイン案がある。公開プロフィールOverviewに表示されるのはmainのREADMEである。

## Next（次）

- 受講生用教材のVisibility・権限と公開可能な更新内容を確認する。
- Visibility変更は未承認のため実施しない。
- プレビュー用ブランチのREADMEをブラウザで確認し、デザインの採用を判断する。

## Blockers（阻害要因）

- 受講生用RepositoryのVisibility・権限等は未確認。
- 前回確認時、限定公開方針とPublicの実状態に不一致があった。Visibilityは未変更。

## Related Decisions（関連Decision）

- なし。2026-10-23の利用者提示「GitHubプロフィール・教材案内ページ整備指示」を今回仕様の根拠とする。
