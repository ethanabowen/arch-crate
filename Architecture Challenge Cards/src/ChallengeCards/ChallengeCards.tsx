import ChallengeCard from "../ChallengeCard/ChallengeCard";
import {
  ChallengeCardDifficulty,
  ChallengeCardFace,
  ChallengeCardData,
} from "../types";
import "./ChallengeCard.css";

type IChallengeCardsProps = {
  challenges: ChallengeCardData[];
  cardFace: ChallengeCardFace;
  difficulty: ChallengeCardDifficulty;
};

function ChallengeCards({ challenges, cardFace, difficulty }: IChallengeCardsProps) {
  return (
    <>
      {challenges.map((challenge, index) => {
        return (
          <ChallengeCard
            cardId={difficulty.toString() + index}
            key={difficulty.toString() + index}
            cardFace={cardFace}
            challengeCardData={challenge}
            difficulty={difficulty}
          />
        );
      })}
    </>
  );
}

export default ChallengeCards;
