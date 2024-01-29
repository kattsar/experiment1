#To assign the same number of trials to each condition per modality, you can modify the code in the following way:
#First, calculate the number of trials per condition and modality. 
#Since there are 4 conditions (repeat type, repeat speak, switch type speak, switch speak type) and 2 modalities (type, speak), you will have a total of 8 combinations of conditions and modalities. 
#In this case, since you want to assign the same number of trials to each condition per modality, you can divide the total number of trials (ntrials) by 8 to get the number of trials per condition per modality.


# Defining the number of conditions and modalities
nconditions <- 4
nmodalities <- 2

# Calculating the number of trials per condition per modality
ntrials_condition_modality <- ntrials/(nconditions*nmodalities)

#Next, you can modify the code that assigns conditions to each pair of trials. 
#Instead of using a series of if-else statements, you can use the case_when function to assign conditions based on the sequence and modality of each pair. 
#You can also add a check to ensure that each condition per modality is assigned the correct number of trials.


# Assigning conditions to each pair of trials
df <- df %>% 
  group_by(block) %>% 
  mutate(pair_no = rep(1:(ntrials/2), each = 2)) %>% 
  ungroup() %>% 
  mutate(
    condition_modality = paste0(condition, modality)
  ) %>% 
  group_by(condition_modality) %>% 
  mutate(
    condition_modality_count = row_number()
  ) %>% 
  ungroup() %>% 
  mutate(
    condition_modality_trial = case_when(
      condition_modality_count <= ntrials_condition_modality ~ "target",
      TRUE ~ "nontarget"
    )
  ) %>% 
  select(-condition_modality_count) %>% 
  group_by(block, pair_no, modality) %>% 
  mutate(
    condition_modality_trial_count = sum(condition_modality_trial == "target")
  ) %>% 
  ungroup() %>% 
  mutate(
    condition_modality_trial = case_when(
      condition_modality_trial == "target" &
        condition_modality_trial_count > ntrials_condition_modality ~ "nontarget",
      TRUE ~ condition_modality_trial
    )
  ) %>% 
  select(-condition_modality_trial_count, -condition_modality) %>% 
  group_by(block, modality, condition) %>% 
  mutate(
    condition_modality_count = sum(condition_modality_trial == "target")
  ) %>% 
  ungroup() %>% 
  mutate(
    condition_modality_trial = case_when(
      condition_modality_trial == "target" &
        condition_modality_count > ntrials_condition_modality ~ "nontarget",
      TRUE ~ condition_modality_trial
    )
  ) %>% 
  select(-condition_modality_count)

#This code first combines the condition and modality into a single column called condition_modality. 
#It then assigns a target or nontarget trial to each pair of trials based on the number of trials assigned to each condition per modality. 
#The code then checks whether each condition per modality has been assigned the correct number of trials and reassigns nontarget trials if necessary. 
#Finally, the code splits the condition_modality column back into separate columns for condition and modality.





k = 1
pairs_per_condition <- floor(ntrials / 4)
n_switch_speak_type <- ntrials - (3 * pairs_per_condition)
n_type <- sum(df$modality == "type")
n_speak <- sum(df$modality == "speak")
n_type_to_assign <- pairs_per_condition - (n_type %% pairs_per_condition)
n_speak_to_assign <- pairs_per_condition - (n_speak %% pairs_per_condition)

for (k in 1:ntrials) {
  #get the sequence for the current pair
  pair_sequence <- df[df$block == j & df$pair_no == k, ]$sequence
  
  #get words and modalities for current pair
  pair_words <- df[df$block == j & df$pair_no == k, ]$word
  pair_modalities <- df[df$block == j & df$pair_no == k, ]$modality
  
  # Check if there are still pairs to be assigned in each condition
  if (n_switch_speak_type > 0) {
    # check if it is a switch speak type pair based on sequence or modality
    if ((pair_sequence[1] == 1 & pair_sequence[2] == 2) || (pair_modalities[1] == "speak" & pair_modalities[2] == "type")) {
      df[df$block == j & df$pair_no == k, ]$condition <- "switch speak type"
      n_switch_speak_type <- n_switch_speak_type - 1
    }
  } else if (n_type_to_assign > 0 && all(pair_sequence == 1) && all(pair_modalities == "type")) {
    df[df$block == j & df$pair_no == k, ]$condition <- "repeat type"
    n_type_to_assign <- n_type_to_assign - 1
  } else if (n_speak_to_assign > 0 && all(pair_sequence == 2) && all(pair_modalities == "speak")) {
    df[df$block == j & df$pair_no == k, ]$condition <- "repeat speak"
    n_speak_to_assign <- n_speak_to_assign - 1
  } else {
    df[df$block == j & df$pair_no == k, ]$condition <- "switch type speak"
  }
  
  # get the current pair's word if k is odd
  if (k %% 2 == 1) { #check if this is the 1st trial in a pair
    pair_word <- ifelse(
      df[df$block == j, ]$sequence[k] %in% c(1),
      final_corpus %>%
        filter(modality == "type") %>%
        sample_n(size = 1) %>%
        pull(word),
      final_corpus %>%
        filter(modality == "speak") %>%
        sample_n(size = 1) %>%
        pull(word)
    )
  }
  df[df$block == j, ]$word[k] <- pair_word
  
  if (k %% 2 == 1) {
    df[df$block == j & df$pair_no == (k+1)/2, ]$condition[1] <- "nontarget"
  }
}
