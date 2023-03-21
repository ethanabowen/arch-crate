export type TriviaCardData = {
  question: string;
  answer: string;
};

export enum TriviaCardFace {
  QUESTION,
  ANSWER,
}

export enum TriviaCardDifficulty {
  PRACTITIONER, ASSOCIATE, PROFESSIONAL, SPECIALTY
}
