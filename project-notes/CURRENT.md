# CURRENT（現在地点）

<details>
<summary>Document Info（文書情報）｜PROFILE-CURRENT-001｜0.4｜Draft</summary>

| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | PROFILE-CURRENT-001 |
| Version（バージョン） | 0.4 |
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
- 2026-10-23：mainの文書・履歴・取得可能なVisibilityを確認し、READMEとCURRENTの修正版を独立した成果物として作成。その後、利用者から対象変更のCommit・Push承認を受領。

## Current（現在）

- 変更前の基準main：9837c7d1229837d332948b60558abe38a3fd8d41。プロフィールはPrivate。
- dokoTsubu-platformはPublic。office-addin-dokotsubu-demoは限定公開方針に対しPublic。
- 受講生用AI教材は現在の接続では取得できず、Visibility・更新内容・受講生権限は未確認。
- README修正版は公開方針と実状態を区別し、講師用正本への生徒向けリンクを削除。手動の更新履歴5件を用意。
- ローカルcloneは資格情報が利用できず未作成。利用者承認に基づき、READMEと本ファイルをGitHub APIでmainへ保存する対象とした。利用者端末の未Commit変更は未確認・非接触。

## Next（次）

- 受講生用教材のVisibility・権限と公開可能な更新内容を確認する。
- Visibility変更は未承認のため実施しない。
- 保存後のGitHub実画面での表示確認は未実施。

## Blockers（阻害要因）

- 現在のGitHub接続では受講生用Repositoryを確認できない。
- 限定公開方針とPublicの実状態に不一致がある。Visibilityは未変更。

## Related Decisions（関連Decision）

- なし。2026-10-23の利用者提示「GitHubプロフィール・教材案内ページ整備指示」を今回仕様の根拠とする。
