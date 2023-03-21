import "./App.css";
import practitioner from "../QandAs/practitioner.json";
import associate from "../QandAs/associate.json";
import professional from "../QandAs/professional.json";
import specialty from "../QandAs/specialty.json";

import { TriviaCardDifficulty, TriviaCardFace } from "../types";
import TriviaCards from "../TriviaCard/TriviaCards";

function App() {
  return (
    <>
      <div className="App Questions">
        <TriviaCards
          qAndAs={practitioner}
          cardFace={TriviaCardFace.QUESTION}
          difficulty={TriviaCardDifficulty.PRACTITIONER}
        />
        <TriviaCards
          qAndAs={associate}
          cardFace={TriviaCardFace.QUESTION}
          difficulty={TriviaCardDifficulty.ASSOCIATE}
        />
        <TriviaCards
          qAndAs={professional}
          cardFace={TriviaCardFace.QUESTION}
          difficulty={TriviaCardDifficulty.PROFESSIONAL}
        />
        <TriviaCards
          qAndAs={specialty}
          cardFace={TriviaCardFace.QUESTION}
          difficulty={TriviaCardDifficulty.SPECIALTY}
        />
      </div>
      <div className="App Answers">
        <TriviaCards
          qAndAs={practitioner}
          cardFace={TriviaCardFace.ANSWER}
          difficulty={TriviaCardDifficulty.PRACTITIONER}
        />
        <TriviaCards
          qAndAs={associate}
          cardFace={TriviaCardFace.ANSWER}
          difficulty={TriviaCardDifficulty.ASSOCIATE}
        />
        <TriviaCards
          qAndAs={professional}
          cardFace={TriviaCardFace.ANSWER}
          difficulty={TriviaCardDifficulty.PROFESSIONAL}
        />
        <TriviaCards
          qAndAs={specialty}
          cardFace={TriviaCardFace.ANSWER}
          difficulty={TriviaCardDifficulty.SPECIALTY}
        />
      </div>
    </>
  );
}

export default App;
