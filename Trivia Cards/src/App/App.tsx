import "./App.css";
import practitioner from "../QandAs/practitioner.json";
import associate from "../QandAs/associate.json";
import professional from "../QandAs/professional.json";
import specialty from "../QandAs/specialty.json";

import { TriviaCardData, TriviaCardDifficulty, TriviaCardFace } from "../types";
import TriviaCards from "../TriviaCards/TriviaCards";

const MAX_TRIVIA_CARDS_PER_PAGE = 24
function firstNElements(jsonList:TriviaCardData[], minIndex: number, maxIndex:number) {
  return jsonList.slice(minIndex,maxIndex)
}

function App() {
  console.log('Practitioner Count: ', practitioner.length)
  console.log('Associate Count: ', associate.length)
  console.log('Professional Count: ', professional.length)
  console.log('Specialty Count: ', specialty.length)

  console.log(firstNElements(practitioner, 0, Math.min(practitioner.length, 20)))
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
      </div>

      <div className="App Questions">
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
