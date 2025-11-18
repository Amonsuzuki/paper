# 60QAの進め方

## 目次 / Table of Contents

- １．はじめに・序論 / Introduction（0/10完了）
- ２．関連研究 / Related Work（0/5完了）
- ３．問題設定 / Problem Statement（0/8完了）
- ４．手法 / Method（0/11完了）
- ５．実験設定 / Experimental Setup（0/11完了）
- ６．実験結果 / Experimental Results（0/14完了）
- ７．結論 / Conclusions（0/3完了）

## 概要 / Overview

標準的な国際会議論文は、およそ60段落からなる。各段落を質問への回答だと考えれば、約60個の質問に答えることで論文を完成できる。

論文全体を考えるから途方に暮れるのであって、各質問に分割すれば楽。

質問者は、査読者（他大学や他分野の教員）と想定する。
具体的な質問者（XX先生、等）を思い浮かべ、その人からメールが届いたと想定して回答する。

### 推奨される執筆順序

「はじめに」からスタートすると詰まるので、以下の順で書くべし。

1. `do {３問題設定} while (完了率<66%);`
2. `do {５実験設定} while (完了率<66%);`
3. `do {４手法} while (完了率<50%);`
4. `do {６実験結果} while (完了率<66%);`
5. `do {３問題設定, ４手法, ５実験設定, ６実験結果} while (完了率<100%);` // 順不同
6. `do {７結論} while (完了率<66%);`
7. `do {１はじめに} while (完了率<66%);` // ここで「はじめに」に着手
8. `do {２関連研究} while (完了率<66%);`
9. `do {１はじめに, ２関連研究, ７結論} while (完了率<100%);` // 順不同

完了したら、TeX流し込み→論理構造の調整→短縮→赤入れ、と進む。

### なぜ順番を守るべきか？

順番を気にせず進むのはなぜ良くないか？
例えば、用語定義等が誤ったまま次に進むと、大量のQAで同じ指摘が発生し、結局手戻りが発生する。

テンプレ質問は最大公約数的な質問なので、自分の論文にそぐわないものもある。
よって、通常１０個程度は質問をカスタマイズか削除する。

### 記号の意味

- **▲**：未完了
- **○**：教員チェック済

### 重要な原則

- 回答の第1文はトピックセンテンスから始めよ。
- 論文執筆はプログラミングのようなものだと思えば良い。
  - 適切なブロック（関数/QA）に分割して、始めから終わりまでのロジックを設計するという意味では同じ。
- 60QAは、文章を書くのが苦手な人でも書ける仕組みとして作った。ただし、京大・ATR・NICTでの所属研究室のノウハウ・査読者からのコメント・先人の知恵に立脚している。

### べからず集

- 単語のみや体言止めや「...であるため。」で回答を終わらせてはならない
- 常に文で回答せよ。
- メールだったら、質問者に単語で回答することなどしないはず。

---

# １．はじめに・序論 / Introduction（0/10完了）

## 1-1. ▲本研究の社会的背景は何か？ / What is the social background?

**ヒント：**
第１文は、読者と共有できる最大公約数的事実から始めることが多い。100人いたら90人賛成するぐらいの文という意味。

以下のようなロジックが理解されやすい。

1. Aは重要である。
   - 読み手「ほぼ賛成」
2. AのうちBにはCという問題がある。Cは難しい。
   - 読み手「まあそういうものかな」
3. 既存研究ではCを解くには不十分であった。本研究では...を提案する。
   - 読み手「了解」

**回答：**


## 1-2. ▲本研究のtarget task/problemは何か？ / What is the target problem of this work?

**回答：**


## 1-3. ▲本研究のtarget problemの具体例（ユースケース）は何か？ / Explain a typical use case.

**回答：**


## 1-4. ▲そのtarget problemが難しいと言う根拠は何か？既存手法が誤る例はどんなケースか？ / Why is this task challenging?

**回答：**


## 1-5. ▲既存手法はなぜ不十分なのか？ / Why are conventional studies insufficient?

**ヒント：**
既存手法として1つだけを引用するのはNG。提案手法が狭い範囲を扱ったように見えるし、著者が不勉強であると受け取られる。
既存手法群の不十分な点を抽象化すべし。

**回答：**


## 1-6. ▲本研究では何を提案し、何を解決するのか？ / What is proposed and solved in this study?

**回答：**


## 1-7. ▲提案手法は既存手法と何が違うのか？主要な違いに絞って述べよ。 / What is the difference between the proposed and conventional methods?

**回答：**


## 1-8. ▲既存手法との違う部分は、なぜ導入するべきなのか？なぜ導入するとうまくいくと予想されるのか？ / Explain why the difference should be introduced.

**回答：**


## 1-9. ▲提案手法の新規性は何か？箇条書きせよ。 / What is the novelty of the proposed method?

**回答：**


## 1-10. ▲提案手法全体の構成をeye-catch figureを用いて示せ（通常6回修正ののち確定）。 / Show the eye-catch figure.

**回答：**

---
# ２．関連研究 / Related Work（0/5完了）

## 2-1. ▲XXX分野のサーベイ論文を複数挙げよ。 / Explain about multiple survey papers in the related area.

**回答：**


## 2-2. ▲論文を複数挙げて、１個目の関連分野を説明せよ。 / Explain the first related subfield and several related papers.

**回答：**


## 2-3. ▲論文を複数挙げて、N個目の関連分野を説明せよ。（この項目を個数分コピーしてください） / Explain the N-th related subfield and several related papers.

**回答：**


## 2-4. ▲XXX分野の標準データセットについて説明せよ。 / Explain standard datasets in the related fields.

**回答：**


## 2-5. ▲提案手法と類似手法A（＋類似手法B、類似手法C）との違いは何か？ / What is the difference(s) between the proposed and related methods?

**回答：**

---
# ３．問題設定 / Problem Statement（0/8完了）

## 3-1. ▲対象とするタスクの名称および内容は何か？ / What is the target problem?

**回答：**


## 3-2. ▲対象タスクの望ましい解・出力について説明せよ（何をもって良い解だとするのか）。 / What is the expected behavior of the system?

**ヒント：**
本タスクでは、…が望ましい。

**回答：**


## 3-3. ▲対象タスクの代表例を示せ（図を付けること）。 / Explain a typical sample with a figure.

**回答：**


## 3-4. ▲このタスクで与えられる入力は何か？ / What are the inputs of the task?

**ヒント：**
提案手法に限らず、どの手法であっても与えられる入力について書く。

**回答：**


## 3-5. ▲タスクで求められる出力は何か？ / What kind of outputs are expected for the task?

**回答：**


## 3-6. ▲使用する用語を定義せよ。 / Define the terms used in the paper.

**回答：**


## 3-7. ▲本研究では何を扱わないか（＝何を前提にしているか）？ / What is the assumption in the paper?

**回答：**


## 3-8. ▲タスクの評価尺度は何か？ / Which metric is used?

**回答：**

---
# ４．手法 / Method（0/11完了）

## 4-1. ▲本研究は何の手法を拡張した何を提案するものか？ / Which method do you extend?

**回答：**


## 4-2. ▲提案手法で行った拡張は、上記の既存手法以外にも広く適用可能であることを説明せよ（＝他の既存手法に適用できないのであれば一般性がない拡張である）。 / Explain that the extensions made in the proposed method are widely applicable to other methods (i.e., if the extension cannot be applied to other methods, it would not be a generalized method).

**回答：**


## 4-3. ▲提案手法と既存手法の違いを箇条書きせよ。 / List the differences between the proposed method and the conventional methods.

**回答：**


## 4-4. ▲提案手法は何個の主要モジュールを有するか？各主要モジュールの名称を示せ。 / How many main modules does the proposed model have? Explain each method briefly.

**ヒント：**
新規性を主張する部分には、査読者に注目してもらえる名前を付けるべし。

**回答：**


## 4-5. ▲提案手法のモデル構造を示せ（図）。 / Explain the structure of the model.

**回答：**


## 4-6. ▲入力を数式（またはx等の記号）で定義し説明せよ。各入力はそれぞれ何次元か？ / Define the input to the proposed method.

**ヒント：**
例えば、「モデルの入力はx_imgである。ここに、x_imgはmagnetogram画像を表す。」のように定義したとする。それにより、曖昧性を減少させると同時にスペースの無駄遣いを回避できる。

**回答：**


## 4-7. ▲どのように入力特徴を抽出したのか（例えばバックボーンネットワークについて説明せよ）？ / Explain how the input features are extracted.

**回答：**


## 4-8. ▲１個目のモジュールのmotivation・役割・入出力・構造を示して説明せよ。 / Explain the motivation, role, input-output, and structure of the 1st module.

**回答：**


## 4-9. ▲N個目のモジュールのmotivation・役割・入出力・構造を示して説明せよ。（この項目を個数分コピーしてください） / Explain the motivation, role, input-output, and structure of the N-th module. (Copy this question if needed)

**回答：**


## 4-10. ▲予測を数式で定義せよ。 / Define the prediction.

**回答：**


## 4-11. ▲損失関数の定義を示せ。 / What is the embedding loss function? What are the alternatives?

**回答：**

---
# ５．実験設定 / Experimental Setup（0/11完了）

## 5-1. ▲（既存データセットを使ったのであれば）何というデータセットを使用したか？（新規構築したのであれば）どのようにデータセットを構築したか？ / Explain about the dataset. If the dataset was constructed in this study, explain how to construct it.

**回答：**


## 5-2. ▲データセットのアノテーション方法（アノテータへ何を指示したか）を示せ。 / Explain about the instructions given to the annotators.

**回答：**


## 5-3. ▲なぜ標準データセットを使わなかったのか？使ったのであれば、なぜ使ったのか？ / Why did not you use the standard data set? If you did, why?

**回答：**


## 5-4. ▲データセットをどのように事前処理（またはデータ拡張）したか？ / How was the dataset pre-processed?

**回答：**


## 5-5. ▲データセットの統計情報を示せ。サンプル数、語彙サイズ（ユニーク語数）、全単語数、平均文長、言語、アノテータの数、シミュレーション or 実機、等について説明せよ。 / Explain about the statistics of the dataset: dataset size, vocabulary size (#unique words), # of total words, average sentence length, language, # of annotators, simulation or real-world.

**回答：**


## 5-6. ▲training set（訓練集合）・validation set（検証集合）・test set（テスト集合）をどのように分割したか？各々のサイズを示せ。 / How was the dataset divided into training set, validation set, and test set? Indicate the size of each.

**回答：**


## 5-7. ▲training set（訓練集合）・validation set（検証集合）・test set（テスト集合）を各々どのように使用したか？ / How was the training set, validation set, and test set each used?

**回答：**


## 5-8. ▲提案手法の設定（最適化手法、エポック数、ハイパーパラメータ等）を表にまとめよ。 / Show a table about experimental setup for the proposed method, such as optimization method, number of epochs, and hyperparameters.

**回答：**


## 5-9. ▲提案手法のパラメータ数と積和演算数（Multiply-add operations）を示せ。 / How many parameters and multiply-add operations does the model have?

**回答：**


## 5-10. ▲訓練に用いたハードウェア構成を示せ。 / Explain about the spec of the machine used in the experiment.

**回答：**


## 5-11. ▲訓練に要した時間を示せ。また、１サンプルあたりの推論に要した時間を示せ。 / How long did it take for training? Explain the inference time per sample.

**回答：**

---
# ６．実験結果 / Experimental Results（0/14完了）

## 6-1. ▲ベースライン手法との定量的比較結果を示せ。 / Show the quantitative comparison results with the baseline method(s).

**ヒント：**
表には何が書かれているのか？縦と横の意味は？数字の意味は？平均と標準偏差なのか？何回実験したのか？Human performanceが存在するなら表示せよ。

**回答：**


## 6-2. ▲何をベースライン手法（群）としたか？ / What was used as the baseline method(s)?

**回答：**


## 6-3. ▲上記ベースラインを選んだ理由を説明せよ。 / Explain the reason for choosing the above baseline(s).

**回答：**


## 6-4. ▲評価尺度（群）について数式で説明せよ。複数あるのであれば、どれが主要尺度か？ / Explain the metric(s) by using equations. Which one is the primary metric?

**回答：**


## 6-5. ▲なぜそれらの評価尺度を使用したのか？他の評価尺度ではダメなのか？ / Why did you use those evaluation metrics? Why not other metrics?

**回答：**


## 6-6. ▲ベースラインと提案手法の性能を（相対的な性能差ではなく）絶対的な値で示せ。 / Show the performance of the baseline and proposed methods in absolute values, not relative performance differences.

**ヒント：**
実験結果説明において、同じ文型をコピペして説明したら不採択になる、と考えるべし。
少なくとも「Similarly」「as well」等を入れる。

**回答：**


## 6-7. ▲実験結果は統計的に有意（p<0.05）であったか？ / Were the experimental results statistically significant (p<0.05)?

**回答：**


## 6-8. ▲定性的結果：提案手法が成功した例（N個）を示せ。Ground Truth、ベースライン手法、提案手法による予測結果をそれぞれ示せ。 / Qualitative results: Show examples (N) of successful cases of the proposed method. Show the Ground Truth, predictions by the baseline method, and predictions by the proposed method respectively.

**ヒント：**
結果の説明だけはNG（＝「読者が勝手に解釈せよ」という意味だから）。どういう点が適切だったのかという解釈と、何を根拠にそう考えるのかを説明せよ。

**回答：**


## 6-9. ▲定性的結果：提案手法が失敗した例（M個、N>M）を示せ。なぜ失敗したのか？ / Qualitative results: Show M examples of failure cases of the proposed method (where N>M). Why did they fail?

**回答：**


## 6-10. ▲Ablation studyにおいて何のために何を取り除いたかを説明せよ。定量的結果に基づき、取り除いた要素が有効だったことを示せ。なぜ有効だったのかを説明せよ。 / Explain what is ablated.

**ヒント：**
意図：Modelに(i)(ii)...のように番号を与えるべし。条件には(i)(ii)をつけてはならない。

本文の内容：
- XXX ablation
  - 説明（何をinvestigateするために、何を取り除いたのか）＋定量的結果＋考察
- YYY ablation
  - 説明＋定量的結果＋考察
- ZZZ ablation
  - ...

Model：
取り除いた結果のモデルをModel (i), Model (ii), ...と命名する。
提案手法とは、(i)(ii)...すべてを指す。(i)(ii)...のうちの１つが提案手法のような書き方はNG。

表の列は以下のようになる：
- Model
- (i)
- (ii)
- ...

**回答：**


## 6-11. ▲混同行列（Confusion matrix）を示せ。 / Show the confusion matrix.

**回答：**


## 6-12. ▲提案手法の失敗例は予測結果の中に合計何サンプルあったか？ / How many failure cases were included in the prediction results?

**回答：**


## 6-13. ▲失敗例を人手でカテゴリに分類せよ。各カテゴリの定義を示せ。 / Classify the failure cases into categories manually. Show the definitions of each category.

**回答：**


## 6-14. ▲失敗の主要な要因（main bottleneck）とpossible solutionについて説明せよ。 / Explain about the main bottleneck and the possible solution.

**回答：**

---
# ７．結論 / Conclusions（0/3完了）

## 7-1. ▲本研究ではどのようなタスクを扱ったか？ / What kind of task was addressed?

**回答：**


## 7-2. ▲本研究の貢献（contributions）を過去形で箇条書きせよ。 / List the contributions of this study in the past tense.

**回答：**


## 7-3. ▲将来研究は何か？ / What is the future study?

**回答：**

