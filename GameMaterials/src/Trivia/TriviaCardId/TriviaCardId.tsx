import "./TriviaCardId.css";

type ITriviaCardIdProps = {
  cardId: string;
};

function TriviaCardId({ cardId }: ITriviaCardIdProps) {
  return (
    <div className="TriviaCardId-Body">
      <div className="TriviaCardId-Text">{cardId}</div>
    </div>
  );
}

export default TriviaCardId;
