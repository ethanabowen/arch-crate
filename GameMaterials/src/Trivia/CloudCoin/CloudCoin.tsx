import "./CloudCoin.css";
import cloud from "./cloud.svg";
import { CardDifficulty } from "../../types";

type ICloudCardProps = {
  difficulty:CardDifficulty
};

let cloudCountReward = (difficulty: CardDifficulty) => {
  switch (difficulty) {
    case CardDifficulty.PRACTITIONER:
      return 1;
    case CardDifficulty.ASSOCIATE:
      return 2;
    case CardDifficulty.PROFESSIONAL:
      return 3;
    case CardDifficulty.SPECIALTY:
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
