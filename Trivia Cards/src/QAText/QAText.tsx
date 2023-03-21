import "./QAText.css";
import { TriviaCardFace } from "../types";
import qIcon from "./q.svg";
import aIcon from "./a.svg";

type IQATextProps = {
  cardFace: TriviaCardFace;
};

function QAText({ cardFace }: IQATextProps) {
  return (
    <div className="QAText-Body">
      {cardFace === TriviaCardFace.QUESTION && (
        <img src={qIcon} className="QAText-Icon" alt="QAText-Icon" />
      )}
      {cardFace === TriviaCardFace.ANSWER && (
        <img src={aIcon} className="QAText-Icon" alt="QAText-Icon" />
      )}
    </div>
  );
}

export default QAText;
