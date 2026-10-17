# HANDOFF（引き継ぎ）

## 現在地（2026-10-17）
- 更級日記：完成。6章19ブロック、総再生 2時間28分。公開済み
  - URL: https://yixinxiangfo.github.io/koten-radio/
- 声：Gacrux / モデル：gemini-3.8-flash-tts（tts/config.json）
- APIキー：無料枠プロジェクトのキーを ~/.zshrc の GEMINI_API_KEY で使用
  - 音声生成は `zsh -ic 'python3 tts/tts.py <台本> <出力mp3>'`（.zshrc を読むため）
  - 無料枠の上限値は未確認（AI Studio の rate-limit 画面で確認できる）。1日19リクエストでは上限に当たらず
- 料金：最初のサンプル4本のみ有料キーで約16円（料金表から計算した額の約2倍が実際に請求された）

## 決めたこと
- タグ：[間をとって] → <long pause>。ほかの演技タグは削除し、style 指示に任せる
- CLAUDE.md とルートの 01-01.txt は .gitignore で公開から外している
- 再生ページ：preload="none"、続きから再生、速度、おやすみタイマー、ロック画面操作

## 未解決
- 総再生が 2.5時間に2分足りない（必要ならどこかの章に1ブロック足す）
- 聴く側の反応はまだ聞いていない

## 次の一手
- 聴いた感想を聞いてから、伊勢物語に進むかを決める
