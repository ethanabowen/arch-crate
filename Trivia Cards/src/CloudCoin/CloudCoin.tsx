import "./CloudCoin.css";
import cloud from "./cloud.svg";
import { TriviaCardDifficulty } from "../types";

type ICloudCardProps = {
  difficulty:TriviaCardDifficulty
};

let cloudCountReward = (difficulty: TriviaCardDifficulty) => {
  switch (difficulty) {
    case TriviaCardDifficulty.PRACTITIONER:
      return 1;
    case TriviaCardDifficulty.ASSOCIATE:
      return 2;
    case TriviaCardDifficulty.PROFESSIONAL:
      return 3;
    case TriviaCardDifficulty.SPECIALTY:
      return 4;
    default:
      return 0;
  }
};

function CloudCoin({difficulty}: ICloudCardProps) {
  return (
    <div className="CloudCoin-Body">
      <img
        src={cloud}
        className="CloudCoin-Icon"
        alt="CloudCoin-Icon"
      />
      <div className="CloudCoin-RewardText">{cloudCountReward(difficulty)}</div>
    </div>
  );
}

export default CloudCoin;
