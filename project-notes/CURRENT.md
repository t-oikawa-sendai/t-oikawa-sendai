# CURRENT（現在地点）

<details>
<summary>Document Info（文書情報）｜PROFILE-CURRENT-001｜0.31｜Draft</summary>

| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | PROFILE-CURRENT-001 |
| Version（バージョン） | 0.31 |
| Status（ステータス） | Draft |
| Created Date（作成日） | 2026-10-18 |
| Last Updated（最終更新日） | 2026-10-27 |
| Owner（管理者） | Takashi Oikawa |
| Related Documents（関連文書） | ../README.md / ../CONSTITUTION.md / ../AGENTS.md |

</details>

## Purpose（目的）

GitHubプロフィールを生徒向け教材の総合入口とし、教材概要・リンク・公開区分・直近5件の更新履歴を案内する。

## Completed（完了）

- 2026-10-27：利用者の続行指示を受け、履歴更新script・テスト・CURRENTの3ファイルをcommit `21fbdfb34d4436b57cf8e095a4bc7ff8744b3a0e` でGitHub `main`へ反映し、3ファイルの本文・Blob SHAを再取得して作業用コピーと一致確認した。講師正本の[sync run 40441606946](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/40441606946)を再実行し成功。配布先のCommitは変わらず、31ファイル・S-IECD本文の配布除外を維持した。通知を受けた[profile run 40448246269](https://github.com/t-oikawa-sendai/t-oikawa-sendai/actions/runs/40448246269)も成功し、READMEだけを自動commit `799220859814fc0932fb5dcbc65daf22e2c88ad9` で更新した。GitHubからREADMEを再取得し、AI教材の更新日が2026-10-27、履歴は日付降順5件、指定2欄以外は変更なしと確認。独立Cloneを自動更新commitまでfast-forwardで同期しcleanを確認した。MacBookの既存Repositoryは未確認・未操作で、利用者が別途確認・同期する。
- 2026-10-27：利用者の「①を実行」に基づき、GitHub `main` = `8db77c8cf77bb411ef73f890c3b0fc8383bf0c34` と一致する独立Clone（開始時clean）で履歴更新scriptを修正した。AI履歴が直近5件から外れた正常状態を許容し、残っているAI履歴の日付不一致と、表示範囲内のAI履歴欠落は引き続きエラーにする。同日境界も扱う。変動するREADMEに依存していたテストを固定入力へ変更し、再発防止項目を含む14件が成功。現行READMEの一時コピーでコマンド実行を確認し、指定2欄だけの更新、5行維持、同日・古い通知の無変更、不正日付・未来日付でのファイル保全を確認した。追跡対象READMEは変更していない。完了範囲は独立Clone上の修正・確認のみで、Commit・Push・Actions再実行は未実施。
- 2026-10-24：公開済みのJEV設計更新（368f107、7fe443f）を確認。プロフィールREADMEのJEV教材更新欄と直近5件の先頭に、初回試験の設計追記を反映し、commit `f0514f1` でGitHub `main` へPushした。GitHub上のREADMEファイルと公開プロフィールOverviewのHTMLで新しい2箇所を確認した。既存の2026-10-23のJEV履歴は残し、最古の2026-10-22のAI活用入門履歴を5件の表から外した。
- 2026-10-24：GitHub `main` の commit `380160527c673751d2c6d5f1516af1c82d1c81b7` から独立した作業ツリーで、設計文書管理入門の見出しから「作成中」を外し、Privateの配布用Repositoryへのリンク・教材の収録状態・直近の更新履歴を現況に合わせた。利用者はREADMEとCURRENTのcommit・pushを明示指示した。公開プロフィールOverviewで、新見出し・配布先リンク・直近5件の表示を確認した。反映結果とcommit識別はGit履歴を正とする。
- 2026-10-24：設計文書管理入門の履歴を加えたREADMEで、直近5件、画像の相対参照、git diff --check を確認した。公開プロフィール画面での表示は未確認。
- 2026-10-18：READMEに公開Repository 8件を掲載しmainへ反映（da53969）。
- 2026-10-18：LEARNING標準の3文書を導入し、3件のリンクに印を付けてmainへ反映（b843382）。
- 2026-10-20：削除予定Repositoryへのリンクを削除してmainへ反映（9837c7d）。
- 2026-10-23：READMEとCURRENTの整備をmainへ反映（fbdc818）。プロフィールRepositoryのPublic・default branch mainと、公開プロフィールOverviewでのREADME「教材案内」表示を確認。ローカルcloneの存在とmainのorigin/mainへの同期を確認。
- 2026-10-23：プロフィールREADMEのデザイン案とバナー画像をプレビュー用ブランチ `preview/profile-readme-design-20261023` に配置。ブラウザでREADMEの表示を確認。mainへの反映は未実施。
- 2026-10-23：プレビュー用READMEの上下181pxのSVG装飾帯を作成してブランチへ反映（40fb27f）。GitHubのブラウザで上部・下部の実表示を確認。mainへの反映は未実施。
- 2026-10-23：プレビュー用READMEの公開範囲とログイン・404案内の文言を修正してブランチへ反映（36ccc61）。GitHubのブラウザで新文言の表示、旧説明の削除、上下バナーの残存を確認。mainへの反映は未実施。
- 2026-10-23：上下181pxのバナーをエンジ系に再配色し、上部中央に「教材案内」を配置してプレビュー用ブランチへ反映（53f28f1）。SVG構文・描画・差分と、GitHubブラウザでのタイトル・上下バナー表示を確認。mainへの反映は未実施。
- 2026-10-23：利用者指定順の5教材一覧をプレビュー用ブランチへ反映（b7102b2）。GitHubブラウザで指定順、Officeデモ除外、設計文書管理入門のリンクなし、JEV・score-readerのリンク、上下バナーと公開範囲案内を確認。mainへの反映は未実施。
- 2026-10-23：上下181pxのバナーを暗い大理石調に変え、案内文とポートフォリオ参考資料2件を加えてプレビュー用ブランチへ反映（0a9ad20）。SVG構文・描画とREADME差分を確認。GitHubブラウザで上部バナー、案内文、参考資料2リンク、5教材の表示を確認。mainへの反映は未実施。
- 2026-10-23：上下バナーを少し明るいチャコール・スレートに調整し、上部タイトルの黒背景を除いた案をプレビュー用ブランチへ反映（a3f07df）。SVG構文・描画と425px幅での文字視認性を確認。GitHubブラウザの狭い表示と広い表示で、上部の白い「教材案内」と下部バナーの実表示を確認。READMEの5教材、参考資料2リンク、案内文の残存も確認。mainへの反映は未実施。
- 2026-10-23：表示確認済みのプレビュー用ブランチをmainへfast-forwardで取り込み（8b43348）、README・上下SVG・CURRENTを反映。取込時点では公開プロフィールOverviewでの新デザイン実表示は未確認。
- 2026-10-23：mainのCommit f5d0138反映後の公開プロフィールOverviewで、明るい大理石調の上部バナー（黒帯なし、白文字可読）、指定順5教材、案内文、ポートフォリオ参考資料2リンク、下部バナーの表示をGitHubブラウザで確認。
- 2026-10-23：受講生用AI教材のPrivate状態と2026-10-22の配布ガイド追加・README更新を確認し、プロフィールREADMEの閲覧状態、教材更新欄、直近5件のローカル修正案を作成（未Commit・未Push）。
- 2026-10-23：AI活用入門の案内と直近5件の更新をmainへ反映（663231e）。公開プロフィールOverviewで、Private・2026-10-22の教材更新と、更新履歴の先頭がAI活用入門、残り4件がどこつぶであることをブラウザで確認。
- 2026-10-23：READMEの楽譜リーダー見出しを「楽譜リーダー（Prototype）」、どこつぶ見出しと更新履歴4行を「DokoTsubu（Springboot Version）」へ統一するローカル修正案を作成（未Commit・未Push）。
- 2026-10-23：両表示名の修正をmainへ反映（9e9b8ce）。公開プロフィールOverviewで「DokoTsubu（Springboot Version）」と「楽譜リーダー（Prototype）」の表示をブラウザで確認。
- 2026-10-23：AI活用入門の説明文をUser指定の文言へ置き換え、READMEだけをmainへ反映（26d86f2f0f2acbb710bc5b50bf42be543691ba18）。公開プロフィールOverviewで指定文言の表示と旧文の非表示をブラウザ確認。
- 2026-10-23：配布先Private Repositoryに実際に反映された更新だけをプロフィール履歴へ反映する受信workflow・script・テストと、User採用済みの指定2欄だけの自動Commit・Push例外（D-001）をmainへ反映（c88a4286da54ae301fb971aadf4ad7a17d7d83cf）。GitHub main上の4ファイルを確認。Actions起動・稼働は未確認。
- 2026-10-23：同日通知による受信workflowの実行が2回成功したことをActionsで確認。新しい配布日によるREADME自動更新は未検証。
- 2026-10-24：READMEへ判断特化型AIサンプルとポートフォリオ参考資料の更新を反映（78e301b、bc6ee14）。
- 2026-10-24：`dokoTsubu-platform` の30文書の文書情報を折りたたみ表示へ変更した公開commit（a309661）を確認し、プロフィールREADMEのDokoTsubu教材更新欄と直近5件へ反映。アプリ機能の変更はない。
- 2026-10-24：READMEのDokoTsubu表示名3箇所を「DokoTsubu（機能追加中）」へ変更し、mainへ反映。

## Current（現在）

- 2026-10-27：修正commit `21fbdfb` と自動更新commit `7992208` はGitHub `main`反映済み。本記録作成時、独立Cloneを `7992208` まで同期してcleanを確認した後、CURRENTだけを更新している。記録の保存結果はGit履歴を正とする。利用者はローカル確認・同期をMacBook側で行うと指定した。実機の存在・保存場所・同期状態は未確認で、Mac miniにRepositoryがないと確認したわけではない。
- S-IECD本文は引き続き生徒向け配布対象外。今回配布先に反映されたのは共通目次 `personas/reference/README.md` の版番号と更新日のみで、それを契機にプロフィール更新が起動した。このscript修正はペルソナ利用の必須条件ではなく、別件の不具合対応である。
- 2026-10-24：既存のローカルCloneをGitHub `main` の `919a06d` までfast-forwardで同期した。その後、READMEのJEV更新を `f0514f1` でPushし、GitHub上のREADMEファイルで反映を確認した。
- プロフィールRepositoryはPublic、default branchはmain。公開プロフィールOverviewにREADME「教材案内」が表示されている。
- 受講生用AI教材はPrivate。2026-10-27の共通目次の版番号・更新日変更まで配布済みと確認した。受講生個別の権限付与状況は未確認。
- READMEは公開方針と実状態を区別し、講師用正本への生徒向けリンクを掲載していない。直近5件を管理し、AI活用入門の指定2欄のみ配布実績に応じた自動更新の対象としている。
- GitHub `main` のREADMEの直近5件は、2026-10-27のAI活用入門、2026-10-24の判断特化型AIサンプル・設計文書管理入門・DokoTsubu、2026-10-23の判断特化型AIサンプル。
- AI活用入門の説明文はmainへ反映済みで、以前の公開プロフィールOverviewでも表示確認済み。直近5件から古いAI履歴が外れると停止した[run 40441625606](https://github.com/t-oikawa-sendai/t-oikawa-sendai/actions/runs/40441625606)の不具合は修正・GitHub反映済み。配布元から再通知した[run 40448246269](https://github.com/t-oikawa-sendai/t-oikawa-sendai/actions/runs/40448246269)の成功とREADME自動更新を確認した。今回の新日付を公開プロフィールOverviewの画面で見る確認は未実施。
- 明るい大理石調の上下バナーと背景なしの上部タイトルはmainに反映済み。公開プロフィールOverviewで、指定順5教材、案内文、ポートフォリオ参考資料2リンクと合わせて表示確認済み。
- 「DokoTsubu（機能追加中）」と「楽譜リーダー（Prototype）」の見出しはmainへ反映済み。DokoTsubuの新しい表示名は公開プロフィールOverviewのHTMLでも確認した。
- 設計文書管理入門の受講生向け配布RepositoryはPrivateのTemplate Repositoryであり、README・説明3文書・設計テンプレート7文書の計11ファイルが収録済みである。受講生個別のアクセスは未確認。

## Next（次）

- 設計文書管理入門のリンク先を、受講生の権限で開けるか確認する。
- 受講生個別の閲覧権限を確認する。
- ローカル確認・同期は利用者がMacBook側で行う。実機で未Commit変更・接続先・branchを確認してから安全に同期する。
- Visibility変更は未承認のため実施しない。

## Blockers（阻害要因）

- 受講生個別の権限付与状況は未確認。
- 設計文書管理入門の受講生向け配布Repositoryへの初回投入は完了した。継続同期の設定と受講生個別のアクセス確認は未実施。
- 今回のGitHub側の停止原因は解消を確認済み。MacBook内の既存Repositoryにはこの環境からアクセスできず、利用者による実機側の存在確認・同期が残る。

## Related Decisions（関連Decision）

- D-001。プロフィール整備の根拠は2026-10-23の利用者提示「GitHubプロフィール・教材案内ページ整備指示」。source側の通知・配布境界は講師正本 `ai-setup-materials/project-notes/DECISIONS.md` のD-072。
