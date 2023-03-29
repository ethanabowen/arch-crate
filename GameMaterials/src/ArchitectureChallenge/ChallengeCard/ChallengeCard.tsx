import {
  CardDifficulty,
  CardFace,
  ChallengeCardData,
} from "../../types";
import "./ChallengeCard.css";

type IChallengeCardProps = {
  cardId: string;
  cardFace: CardFace;
  challengeCardData: ChallengeCardData;
  difficulty: CardDifficulty;
};

function ChallengeCard(challengeCard: IChallengeCardProps) {
  const { question, answer } = challengeCard.challengeCardData;

  return (
    <div className="ChallengeCard">
      {/* Questions */}
      {challengeCard.cardFace === CardFace.QUESTION && question && (
        <div className="ChallengeCard-Text">
          {question}
        </div>
      )}

      {/* Answers */}
      {challengeCard.cardFace === CardFace.ANSWER && answer && (
        <>
          <div className="ChallengeCard-Text">
            {answer}
          </div>
          {/* <challengeCardId
            cardId={calcCardIdShortHand(
              challengeCard.difficulty,
              challengeCard.cardId
            )}
          /> */}
        </>
      )}

      {/* <CloudCoin difficulty={challengeCard.difficulty} /> */}
    </div>
  );
}

export default ChallengeCard;
