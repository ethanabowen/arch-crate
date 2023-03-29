import "./TriviaCardPage.css";
import practitioner from "../QandAs/practitioner.json";
import associate from "../QandAs/associate.json";
import professional from "../QandAs/professional.json";
import specialty from "../QandAs/specialty.json";

import { TriviaCardData, CardDifficulty, CardFace } from "../../types";
import TriviaCards from "../TriviaCards/TriviaCards";

const MAX_TRIVIA_CARDS_PER_TriviaCardPage = 24
function firstNElements(jsonList:TriviaCardData[], minIndex: number, maxIndex:number) {
  return jsonList.slice(minIndex,maxIndex)
}

function TriviaCardPage() {
  console.log('Practitioner Count: ', practitioner.length)
  console.log('Associate Count: ', associate.length)
  console.log('Professional Count: ', professional.length)
  console.log('Specialty Count: ', specialty.length)

  console.log(firstNElements(practitioner, 0, Math.min(practitioner.length, 20)))
  return (
    <>
      <div className="TriviaCardPage Questions">
        <TriviaCards
          qAndAs={practitioner}
          cardFace={CardFace.QUESTION}
          difficulty={CardDifficulty.PRACTITIONER}
        />
        <TriviaCards
          qAndAs={associate}
          cardFace={CardFace.QUESTION}
          difficulty={CardDifficulty.ASSOCIATE}
        />
      </div>
      <div className="TriviaCardPage Answers">
        <TriviaCards
          qAndAs={practitioner}
          cardFace={CardFace.ANSWER}
          difficulty={CardDifficulty.PRACTITIONER}
        />
        <TriviaCards
          qAndAs={associate}
          cardFace={CardFace.ANSWER}
          difficulty={CardDifficulty.ASSOCIATE}
        />
      </div>

      <div className="TriviaCardPage Questions">
        <TriviaCards
          qAndAs={professional}
          cardFace={CardFace.QUESTION}
          difficulty={CardDifficulty.PROFESSIONAL}
        />
        <TriviaCards
          qAndAs={specialty}
          cardFace={CardFace.QUESTION}
          difficulty={CardDifficulty.SPECIALTY}
        />
      </div>
      <div className="TriviaCardPage Answers">
        <TriviaCards
          qAndAs={professional}
          cardFace={CardFace.ANSWER}
          difficulty={CardDifficulty.PROFESSIONAL}
        />
        <TriviaCards
          qAndAs={specialty}
          cardFace={CardFace.ANSWER}
          difficulty={CardDifficulty.SPECIALTY}
        />
      </div>
    </>
  );
}

export default TriviaCardPage;
