import ChallengeCard from "../ChallengeCard/ChallengeCard";
import {
  CardDifficulty,
  CardFace,
  ChallengeCardData,
} from "../../types";
import "./ChallengeCards.css";

type IChallengeCardsProps = {
  challenges: ChallengeCardData[];
  cardFace: CardFace;
  difficulty: CardDifficulty;
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
