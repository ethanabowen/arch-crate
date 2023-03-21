export type ChallengeCardData = {
  question: string;
  answer: string;
};

export enum ChallengeCardFace {
  QUESTION,
  ANSWER,
}

export enum ChallengeCardDifficulty {
  PRACTITIONER, ASSOCIATE, PROFESSIONAL, SPECIALTY
}
