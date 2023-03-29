import "./QAText.css";
import { CardFace } from "../../types";
import qIcon from "./q.svg";
import aIcon from "./a.svg";

type IQATextProps = {
  cardFace: CardFace;
};

function QAText({ cardFace }: IQATextProps) {
  return (
    <div className="QAText-Body">
      {cardFace === CardFace.QUESTION && (
        <img src={qIcon} className="QAText-Icon" alt="QAText-Icon" />
      )}
      {cardFace === CardFace.ANSWER && (
        <img src={aIcon} className="QAText-Icon" alt="QAText-Icon" />
      )}
    </div>
  );
}

export default QAText;
