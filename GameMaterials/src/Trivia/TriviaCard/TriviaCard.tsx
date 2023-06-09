import "./TriviaCard.css";
import CloudCoin from "../CloudCoin/CloudCoin";
import { TriviaCardData, CardDifficulty, CardFace } from "../../types";
import QAText from "../QAText/QAText";
import TriviaCardId from "../TriviaCardId/TriviaCardId";

type ITriviaCardProps = {
  cardId: string;
  cardFace: CardFace;
  triviaCardData: TriviaCardData;
  difficulty: CardDifficulty;
};

function calcFontSize(textLength: number) {
  // if(textLength < 20) return 25;
  // else if(textLength < 40) return 20;
  // else if(textLength < 60) return 15;
  // else if(textLength < 80) return 15;

  return 16;
}

function calcBorderColor(difficulty: CardDifficulty) {
  switch (difficulty) {
    case CardDifficulty.PRACTITIONER:
      return "#4f5965"; // Greyish
    case CardDifficulty.ASSOCIATE:
      return "#3a3bf6"; // Light Blue
    case CardDifficulty.PROFESSIONAL:
      return "#068195"; // Teal
    case CardDifficulty.SPECIALTY:
      return "#5536ba"; // Purple
    default:
      return "#ff9900"; // AWS Orange
  }
}

function calcCardIdShortHand(difficulty: CardDifficulty, cardId: string) {
  return CardDifficulty[difficulty].toString().charAt(0).toString() + cardId
}

function TriviaCard(triviaCard: ITriviaCardProps) {
  const { question, answer } = triviaCard.triviaCardData;

  return (
    <div
      className="TriviaCard"
      style={{
        fontSize: calcFontSize(question.length) + "px",
        border: "4px solid " + calcBorderColor(triviaCard.difficulty),
      }}
    >
      <QAText cardFace={triviaCard.cardFace} />

      {/* Questions */}
      {triviaCard.cardFace === CardFace.QUESTION && question && (
        <div
          className="TriviaCard-Text"
          style={{ fontSize: calcFontSize(question.length) + "px" }}
        >
          {question}
        </div>
      )}

      {/* Answers */}
      {triviaCard.cardFace === CardFace.ANSWER && answer && (
        <>
          <div
            className="TriviaCard-Text"
            style={{ fontSize: calcFontSize(answer.length) + "px" }}
          >
            {answer}
          </div>
          <TriviaCardId cardId={calcCardIdShortHand(triviaCard.difficulty, triviaCard.cardId)} />
        </>
      )}

      <CloudCoin difficulty={triviaCard.difficulty} />
    </div>
  );
}

export default TriviaCard;
