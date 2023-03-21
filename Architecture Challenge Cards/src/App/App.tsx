import "./App.css";
import practitioner from "../Architectures/practitioner.json";
import associate from "../Architectures/associate.json";
import professional from "../Architectures/professional.json";
import specialty from "../Architectures/specialty.json";
import ChallengeCard from "../ChallengeCard/ChallengeCard";
import { ChallengeCardDifficulty, ChallengeCardFace } from "../types";
import ChallengeCards from "../ChallengeCards/ChallengeCards";

function App() {
  return (
    <>
      <div className="App Questions">
        <ChallengeCards
          challenges={associate}
          cardFace={ChallengeCardFace.QUESTION}
          difficulty={ChallengeCardDifficulty.ASSOCIATE}
        />
      </div>
      {/* <div className="App Answers">
        <TriviaCards
          qAndAs={practitioner}
          cardFace={TriviaCardFace.ANSWER}
          difficulty={TriviaCardDifficulty.PRACTITIONER}
        />
        
      </div> */}
    </>
  );
}

export default App;
