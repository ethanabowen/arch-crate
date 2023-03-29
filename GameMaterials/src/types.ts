export type TriviaCardData = {
  question: string;
  answer: string;
};

export type ChallengeCardData = {
  question: string;
  answer: string;
};

export enum CardFace {
  QUESTION,
  ANSWER,
}

export enum CardDifficulty {
  PRACTITIONER, ASSOCIATE, PROFESSIONAL, SPECIALTY
}
