CHAT_LEVEL_FEATURES = [
    "positive_bert", "negative_bert", "neutral_bert", "num_words", "num_chars","info_exchange_zscore_chats",
    "discrepancies_lexical_wordcount", "hear_lexical_wordcount", "home_lexical_wordcount",
    "conjunction_lexical_wordcount", "certainty_lexical_wordcount", "inclusive_lexical_wordcount",
    "bio_lexical_wordcount", "achievement_lexical_wordcount", "adverbs_lexical_wordcount",
    "anxiety_lexical_wordcount", "third_person_lexical_wordcount", "negation_lexical_wordcount",
    "swear_lexical_wordcount", "death_lexical_wordcount", "health_lexical_wordcount",
    "see_lexical_wordcount", "body_lexical_wordcount", "family_lexical_wordcount",
    "negative_affect_lexical_wordcount", "quantifier_lexical_wordcount",
    "positive_affect_lexical_wordcount", "insight_lexical_wordcount", "humans_lexical_wordcount",
    "present_tense_lexical_wordcount", "future_tense_lexical_wordcount",
    "past_tense_lexical_wordcount", "relative_lexical_wordcount", "sexual_lexical_wordcount",
    "inhibition_lexical_wordcount", "sadness_lexical_wordcount", "social_lexical_wordcount",
    "indefinite_pronoun_lexical_wordcount", "religion_lexical_wordcount", "work_lexical_wordcount",
    "money_lexical_wordcount", "causation_lexical_wordcount", "anger_lexical_wordcount",
    "first_person_singular_lexical_wordcount", "feel_lexical_wordcount",
    "tentativeness_lexical_wordcount", "exclusive_lexical_wordcount", "verbs_lexical_wordcount",
    "friends_lexical_wordcount", "article_lexical_wordcount", "argue_lexical_wordcount",
    "auxiliary_verbs_lexical_wordcount", "cognitive_mech_lexical_wordcount",
    "preposition_lexical_wordcount", "first_person_plural_lexical_wordcount",
    "percept_lexical_wordcount", "second_person_lexical_wordcount", "positive_words_lexical_wordcount",
    "first_person_lexical_wordcount", "nltk_english_stopwords_lexical_wordcount",
    "hedge_words_lexical_wordcount", "num_question_naive", "NTRI", "word_TTR",
    "first_pronouns_proportion", "function_word_accommodation", "content_word_accommodation",
    "hedge_naive", "textblob_subjectivity", "textblob_polarity", "positivity_zscore_chats", "dale_chall_score", "time_diff",
    "please_politeness_convokit", "please_start_politeness_convokit", "hashedge_politeness_convokit", "indirect_btw_politeness_convokit", "hedges_politeness_convokit", "factuality_politeness_convokit", "deference_politeness_convokit",
    "gratitude_politeness_convokit", "apologizing_politeness_convokit", "1st_person_pl_politeness_convokit", "1st_person_politeness_convokit", "1st_person_start_politeness_convokit", "2nd_person_politeness_convokit",
    "2nd_person_start_politeness_convokit", "indirect_greeting_politeness_convokit", "direct_question_politeness_convokit", "direct_start_politeness_convokit", "haspositive_politeness_convokit",
    "hasnegative_politeness_convokit", "subjunctive_politeness_convokit", "indicative_politeness_convokit", "Acknowledgement_receptiveness_yeomans", "Affirmation_receptiveness_yeomans", "Agreement_receptiveness_yeomans",
    "Apology_receptiveness_yeomans", "Ask_Agency_receptiveness_yeomans", "By_The_Way_receptiveness_yeomans", "Can_You_receptiveness_yeomans", "Conjunction_Start_receptiveness_yeomans", "Could_You_receptiveness_yeomans",
    "Disagreement_receptiveness_yeomans", "Filler_Pause_receptiveness_yeomans", "First_Person_Plural_receptiveness_yeomans", "First_Person_Single_receptiveness_yeomans", "For_Me_receptiveness_yeomans",
    "For_You_receptiveness_yeomans", "Formal_Title_receptiveness_yeomans", "Give_Agency_receptiveness_yeomans", "Goodbye_receptiveness_yeomans", "Gratitude_receptiveness_yeomans", "Hedges_receptiveness_yeomans", "Hello_receptiveness_yeomans",
    "Impersonal_Pronoun_receptiveness_yeomans", "Informal_Title_receptiveness_yeomans", "Let_Me_Know_receptiveness_yeomans", "Negation_receptiveness_yeomans", "Negative_Emotion_receptiveness_yeomans",
    "Please_receptiveness_yeomans", "Positive_Emotion_receptiveness_yeomans", "Reasoning_receptiveness_yeomans", "Reassurance_receptiveness_yeomans", "Second_Person_receptiveness_yeomans", "Subjectivity_receptiveness_yeomans",
    "Swearing_receptiveness_yeomans", "Truth_Intensifier_receptiveness_yeomans", "Bare_Command_receptiveness_yeomans", "YesNo_Questions_receptiveness_yeomans", "WH_Questions_receptiveness_yeomans",
    "Adverb_Limiter_receptiveness_yeomans", "Token_count_receptiveness_yeomans", "certainty_rocklage", "num_all_caps", "num_links",
    "num_reddit_users", "num_emphasis", "num_bullet_points", "num_numbered_points",
    "num_line_breaks", "num_quotes", "num_block_quote_responses", "num_ellipses", "num_parentheses",
    "num_emoji", "mimicry_bert","moving_mimicry","forward_flow"        
]

# TODO: this list isn't reproducible; we need to change it
# TOPIC_FEATURES = [
#     'Residual Topic', 'Trump', 'Gender', 'Government, War and Taxes', 'Abortion', 
#     'Sexual Violence', 'Veganism', 'Education', 'Gun Violence', 'Drugs and Alcohol', 
#     'Art and Movies', 'Depression, Suffering, Suicide', 'The Universe and Space', 
#     'Gaming', 'Copyright and Piracy', 'Gender, Sports and Military', 'Food', 
#     'Tipping Culture', 'Restrooms', 'Marriage, Divorce and Relationships', 
#     'Intelligence', 'Israel-Palestine', 'Sports', 'Bullying', 'Superheros', 
#     'Aircrafts', 'Metrics versus imperial systems', 'Cutlery and Dining', 
#     'Coding and Code Editors', 'Tattoos', 'Clocks and Batteries'
# ]

CONV_LEVEL_FEATURES = [
    'sum_num_words',
    'sum_num_chars',
    'sum_num_messages',
    'gini_coefficient_sum_num_words',
    'gini_coefficient_sum_num_chars',
    'gini_coefficient_sum_num_messages',
    'turn_taking_index',
    'team_burstiness',
    'info_diversity',
    'discursive_diversity',
    'variance_in_DD',
    'incongruent_modulation',
    'within_person_disc_range',
]

CHAT_LEVEL_EXPRESSION = [
    "positive_bert",
    "negative_bert",
    "discrepancies_lexical_wordcount",  
    "neutral_bert",
    "num_words",
    "num_chars",
    "conjunction_lexical_wordcount",
    "certainty_lexical_wordcount",
    "inclusive_lexical_wordcount",
    "bio_lexical_wordcount",
    "adverbs_lexical_wordcount",
    "third_person_lexical_wordcount",
    "negation_lexical_wordcount",
    "swear_lexical_wordcount",
    "negative_affect_lexical_wordcount",
    "quantifier_lexical_wordcount",
    "positive_affect_lexical_wordcount",
    "present_tense_lexical_wordcount",
    "future_tense_lexical_wordcount",
    "past_tense_lexical_wordcount",
    "inhibition_lexical_wordcount",
    "sadness_lexical_wordcount",
    "social_lexical_wordcount",
    "indefinite_pronoun_lexical_wordcount",
    "anger_lexical_wordcount",
    "first_person_singular_lexical_wordcount",
    "feel_lexical_wordcount",
    "tentativeness_lexical_wordcount",
    "exclusive_lexical_wordcount",
    "verbs_lexical_wordcount",
    "article_lexical_wordcount",
    "argue_lexical_wordcount",
    "auxiliary_verbs_lexical_wordcount",
    "cognitive_mech_lexical_wordcount",
    "preposition_lexical_wordcount",
    "first_person_plural_lexical_wordcount",
    "second_person_lexical_wordcount",
    "positive_words_lexical_wordcount",
    "first_person_lexical_wordcount",
    "nltk_english_stopwords_lexical_wordcount",
    "hedge_words_lexical_wordcount",
    "num_question_naive",
    "NTRI",
    "word_TTR",
    "first_pronouns_proportion",
    "function_word_accommodation",
    "hedge_naive",
    "textblob_subjectivity",
    "textblob_polarity",
    "positivity_zscore_chats",
    "dale_chall_score",
    "time_diff",
    "please_politeness_convokit",
    "please_start_politeness_convokit",
    "hashedge_politeness_convokit",
    "indirect_btw_politeness_convokit",
    "hedges_politeness_convokit",
    "factuality_politeness_convokit",
    "deference_politeness_convokit",
    "gratitude_politeness_convokit",
    "apologizing_politeness_convokit",
    "1st_person_pl_politeness_convokit",
    "1st_person_politeness_convokit",
    "1st_person_start_politeness_convokit",
    "2nd_person_politeness_convokit",
    "2nd_person_start_politeness_convokit",
    "indirect_greeting_politeness_convokit",
    "direct_question_politeness_convokit",
    "direct_start_politeness_convokit",
    "haspositive_politeness_convokit",
    "hasnegative_politeness_convokit",
    "subjunctive_politeness_convokit",
    "indicative_politeness_convokit",
    "Acknowledgement_receptiveness_yeomans",
    "Affirmation_receptiveness_yeomans",
    "Agreement_receptiveness_yeomans",
    "Apology_receptiveness_yeomans",
    "Ask_Agency_receptiveness_yeomans",
    "By_The_Way_receptiveness_yeomans",
    "Can_You_receptiveness_yeomans",
    "Conjunction_Start_receptiveness_yeomans",
    "Could_You_receptiveness_yeomans",
    "Disagreement_receptiveness_yeomans",
    "Filler_Pause_receptiveness_yeomans",
    "First_Person_Plural_receptiveness_yeomans",
    "First_Person_Single_receptiveness_yeomans",
    "For_Me_receptiveness_yeomans",
    "For_You_receptiveness_yeomans",
    "Formal_Title_receptiveness_yeomans",
    "Give_Agency_receptiveness_yeomans",
    "Goodbye_receptiveness_yeomans",
    "Gratitude_receptiveness_yeomans",
    "Hedges_receptiveness_yeomans",
    "Hello_receptiveness_yeomans",
    "Impersonal_Pronoun_receptiveness_yeomans",
    "Informal_Title_receptiveness_yeomans",
    "Let_Me_Know_receptiveness_yeomans",
    "Negation_receptiveness_yeomans",
    "Negative_Emotion_receptiveness_yeomans",
    "Please_receptiveness_yeomans",
    "Positive_Emotion_receptiveness_yeomans",
    "Reasoning_receptiveness_yeomans",
    "Reassurance_receptiveness_yeomans",
    "Second_Person_receptiveness_yeomans",
    "Subjectivity_receptiveness_yeomans",
    "Swearing_receptiveness_yeomans",
    "Truth_Intensifier_receptiveness_yeomans",
    "Bare_Command_receptiveness_yeomans",
    "YesNo_Questions_receptiveness_yeomans",
    "WH_Questions_receptiveness_yeomans",
    "Adverb_Limiter_receptiveness_yeomans",
    "Token_count_receptiveness_yeomans",
    "certainty_rocklage",
    "num_all_caps",
    "num_reddit_users",
    "num_emphasis",
    "num_bullet_points",
    "num_numbered_points",
    "num_line_breaks",
    "num_ellipses",
    "num_parentheses",
    "num_emoji"
]

CHAT_LEVEL_CONTENT = ["info_exchange_zscore_chats",  "hear_lexical_wordcount",    "home_lexical_wordcount",    "achievement_lexical_wordcount",    "anxiety_lexical_wordcount",    "death_lexical_wordcount",    "health_lexical_wordcount",    "see_lexical_wordcount",    "body_lexical_wordcount",    "family_lexical_wordcount",    "insight_lexical_wordcount",    "humans_lexical_wordcount",    "relative_lexical_wordcount",    "sexual_lexical_wordcount",    "religion_lexical_wordcount",    "work_lexical_wordcount",    "money_lexical_wordcount",    "causation_lexical_wordcount",    "friends_lexical_wordcount",    "percept_lexical_wordcount",    "num_links",    "num_quotes",    "num_block_quote_responses",    "mimicry_bert",
    "moving_mimicry",
    "forward_flow","content_word_accommodation"]


CONV_LEVEL_EXPRESSION = ['turn_taking_index','gini_coefficient_sum_num_words',
    'gini_coefficient_sum_num_chars',
    'gini_coefficient_sum_num_messages','team_burstiness']

CONV_LEVEL_CONTENT = [
    'sum_num_words',
    'sum_num_chars',
    'sum_num_messages',
    'info_diversity',
    'discursive_diversity',
    'variance_in_DD',
    'incongruent_modulation',
    'within_person_disc_range']

EXPRESSION_ONLY_1 = CHAT_LEVEL_EXPRESSION + CONV_LEVEL_EXPRESSION
# CONTENT_TOPICS_ONLY_2 = TOPIC_FEATURES
CONTENT_SEMANTIC_ONLY_3 = CHAT_LEVEL_CONTENT + CONV_LEVEL_CONTENT
# CONTENT_TOPICS_AND_SEMANTIC_4 = CONTENT_TOPICS_ONLY_2 + CONTENT_SEMANTIC_ONLY_3
EXPRESSION_AND_SEMANTIC_SIMILARITY_5 = EXPRESSION_ONLY_1 + CONTENT_SEMANTIC_ONLY_3
# ALL_FEATURES_6 = EXPRESSION_ONLY_1 + CONTENT_TOPICS_AND_SEMANTIC_4


# Assign equal weights to each chat in a conversation
def compute_weights(df):
    row_counts = df['conversation_num'].value_counts()
    df['weights'] = df['conversation_num'].map(lambda x: 1 / row_counts[x])


def aggregate_chat_level_features(df_chat, df_conv):
    # Ensure 'message' column contains only strings
    df_chat['message'] = df_chat['message'].astype(str)
    
    # Aggregate weighted features and concatenate messages
    aggregated_cols = (
        df_chat.assign(**{col: df_chat[col] * df_chat['weights'] for col in CHAT_LEVEL_FEATURES})  # Weighted features
        .groupby('conversation_num', as_index=False)
        .agg({**{col: 'sum' for col in CHAT_LEVEL_FEATURES},  # Sum weighted values
              'message': ' '.join})  # Concatenate messages
    )
    
    # Ensure we get the first occurrence of 'outcome' for each conversation_num
    outcomes = df_chat.groupby('conversation_num')['outcome'].first().reset_index()
    aggregated_cols = aggregated_cols.merge(outcomes, on='conversation_num', how='inner')

    # Merge with conversation-level features
    result = aggregated_cols.merge(
        df_conv[['conversation_num'] + CONV_LEVEL_FEATURES],  # Include 'conversation_num' and conv level features
        on='conversation_num',
        how='inner'
    )
    
    return result
