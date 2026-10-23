# DECISIONS（判断記録）

## D-001 Limit Automated Profile Commits to Distributed AI Material History（自動Commitを配布済みAI教材の履歴に限定する）

Date（日付）: 2026-10-23
Related Documents（関連文書）: README.md / .github/workflows/update-student-history.yml / scripts/update_profile_history.py / project-notes/CURRENT.md / 講師正本 `ai-setup-materials` の D-072

Decision（決定）:
- `OSLIB21-materials/ai-setup-materials-student` のPrivate配布先 `main` に実際に反映された更新だけを、プロフィールREADMEの「AI活用入門」の教材更新日・変更概要と「最近の更新（直近5件）」へ自動反映する。講師正本の変更だけでは公開しない。
- 講師正本の同期workflowから日付だけを受ける `repository_dispatch` 方式を採用する。Private教材の本文・Commit SHA・message・ファイル名を公開payload/READMEへ載せず、Private Repositoryの読取Credentialもプロフィール側へ置かない。受信側は自身の `GITHUB_TOKEN` のContents:writeだけでREADMEを更新する。
- 新しい日付のみ定型文「受講生向け教材の配布内容を更新しました。」をAI欄と履歴に記し、日付降順の5行を維持する。同日・古い通知は無変更として既存の2026-10-22の個別要約を保全する。未来日付または想定外の表形式は失敗とし、READMEを保存しない。
- Userはこの設定差分のCommit・Pushと、以後の受信workflowによる自動Commit・Pushを**READMEの上記2欄だけ**に限って明示承認した。READMEの他の教材欄、別ファイル、人手作業に関する通常の個別承認規則は維持する。受信workflow単独の手動起動や日付手入力は設けず、手動復旧は講師正本側の同期workflowを再実行する。

Rationale（理由）:
実際に配布された教材の更新だけを生徒向け入口へ表示し、Private教材の内部情報と既存の正確な履歴を保護するため。

Evidence（根拠）:
- Userは「受講生用への反映だけ」を対象と決め、2026-10-23に通知・認証方式と狭い自動Commit・Push例外を採用し、両Repositoryの設定Commit・Pushを承認した。
- ローカル草案の基点は `main` = `origin/main` = `c4f78d8d69e3280c53253f1f3a47269f91168823`、clean。

Non-Changes（非変更範囲）:
- 現在のREADME本文・更新履歴、他教材、SVG、Private配布先、既存の通常作業のGit承認規則。稼働確認前はREADMEの「手動管理」コメントを変更しない。

Unverified（未確認）:
- このローカル記録だけでは設定Commit・Push、Secret登録、GitHub Actionsの実行と自動Commit、公開プロフィールの実表示を確認済みにしない。
