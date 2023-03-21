import "./challengeCard.css";

type IChallengeCardProps = {
  cardId: string;
  cardFace: ChallengeCardFace;
  triviaCardData: ChallengeCardData;
  difficulty: ChallengeCardDifficulty;
};

function ChallengeCard(challengeCard: IChallengeCardProps) {
  const { question, answer } = challengeCard.challengeCardData;

  return (
    <div className="challengeCard">
      {/* Questions */}
      {challengeCard.cardFace === challengeCardFace.QUESTION && question && (
        <div
          className="challengeCard-Text"
          style={{ fontSize: calcFontSize(question.length) + "px" }}
        >
          {question}
        </div>
      )}

      {/* Answers */}
      {challengeCard.cardFace === challengeCardFace.ANSWER && answer && (
        <>
          <div
            className="challengeCard-Text"
            style={{ fontSize: calcFontSize(answer.length) + "px" }}
          >
            {answer}
          </div>
          <challengeCardId cardId={calcCardIdShortHand(challengeCard.difficulty, challengeCard.cardId)} />
        </>
      )}

      <CloudCoin difficulty={challengeCard.difficulty} />
    </div>
  );
}

export default ChallengeCard;
