import "./TriviaCards.css";
import { TriviaCardData, TriviaCardDifficulty, TriviaCardFace } from "../types";
import TriviaCard from "../TriviaCard/TriviaCard";

type ITriviaCardsProps = {
  qAndAs: TriviaCardData[];
  cardFace: TriviaCardFace;
  difficulty: TriviaCardDifficulty;
};

function TriviaCards({ qAndAs, cardFace, difficulty }: ITriviaCardsProps) {
  return (
    <>
      {qAndAs.map((qAndA, index) => {
        return (
          <TriviaCard
            cardId={difficulty.toString() + index}
            key={difficulty.toString() + index}
            cardFace={cardFace}
            triviaCardData={qAndA}
            difficulty={difficulty}
          />
        );
      })}
    </>
  );
}

export default TriviaCards;
