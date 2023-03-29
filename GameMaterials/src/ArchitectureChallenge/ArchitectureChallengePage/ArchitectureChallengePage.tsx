import "./ArchitectureChallengePage.css";
import practitioner from "../Architectures/practitioner.json";
import associate from "../Architectures/associate.json";
import professional from "../Architectures/professional.json";
import specialty from "../Architectures/specialty.json";
import ChallengeCard from "../ChallengeCard/ChallengeCard";
import { CardDifficulty, CardFace } from "../../types";
import ChallengeCards from "../ChallengeCards/ChallengeCards";

function ArchitectureChallengePage() {
  return (
    <>
      <div className="ArchitectureChallengePage Questions">
        <ChallengeCards
          challenges={associate}
          cardFace={CardFace.QUESTION}
          difficulty={CardDifficulty.ASSOCIATE}
        />
      </div>
      {/* <div className="ArchitectureChallengePage Answers">
        <TriviaCards
          qAndAs={practitioner}
          cardFace={CardFace.ANSWER}
          difficulty={CardDifficulty.PRACTITIONER}
        />
        
      </div> */}
    </>
  );
}

export default ArchitectureChallengePage;
