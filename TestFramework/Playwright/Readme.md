# PlayWirght E2E TestFramework 操作手順

## プロジェクトの操作コマンド

### Playwrightをインストールする 
- `npm install`
    > プロジェクトの依頼をインストールする。
- `npx playwright install`
    > ブラウザのコーアをインストールする。

### Allureをインストールする
- `Set-ExecutionPolicy RemoteSigned -scope CurrentUser`
- `iwr -useb get.scoop.sh | iex`
- `scoop install allure`
    > ScoopというWindowのPackage ManagerでAllureをインストールする。

### コマンドリスト

- `npm run update`
    > `screenShotDiffWith` 執行するために要たScreenshotをUpdateする。
- `npm run test`
  > wuiTestにいたtestCaseを執行する。**ScreenDiffが要るなら、先に上記のコマンドを執行してください。
- `npm run generate`
  > リポートを生成して、更に対応した分析結果にWeb画面で表示する。

## テストゲスの書き方
    


## グローバルテスト設定


