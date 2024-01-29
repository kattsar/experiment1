############################################################################
# Pseudo-randomisation of trials order in a task-switching paradigm
# Adapted from https://users.fmrib.ox.ac.uk/~behrens/Bakermans2021.pdf
# And https://github.com/jbakermans/stimulus-history-euler-tours
# ----------------------------------------------------------------------
# OSF project: https://osf.io/7kwv6/
# Written by Ladislas Nalborczyk
# E-mail: ladislas.nalborczyk@gmail.com
# Last updated on November 29, 2021
#####################################################################

library(reticulate)
library(tidyverse)
library(forcats)

# We have 4 conditions
# 1: imagined left hand
# 2: imagined right hand
# 3: executed left hand
# 4: executed right hand

# Which gives 16 possible sequences (i.e., pairs of successive trials)
expand.grid(1:4, 1:4)

# But if we treat the left and right hand similarly, we have 8 possible sequences
# 1: current trial imagined some hand - previous trial imagined same hand
# 2: current trial imagined some hand - previous trial imagined other hand
# 3: current trial imagined some hand - previous trial executed same hand
# 4: current trial imagined some hand - previous trial executed other hand
# 5: current trial executed some hand - previous trial imagined same hand
# 6: current trial executed some hand - previous trial imagined other hand
# 7: current trial executed some hand - previous trial executed same hand
# 8: current trial executed some hand - previous trial executed other hand

# Importing the euler package
source_python("euler.py")

# Generating a sequence of four stimuli with 4 repetitions of each pair
# experiment <- Euler(stimuli = 4, pair_repeats = 4)
# sequences <- as.numeric(experiment$get_sequence() ) + 1
# sequences

# Checking the frequency of each pair
# cbind(sequences[-length(sequences)], sequences[-1]) %>%
#     data.frame %>%
#     mutate(X3 = paste(X1, X2) ) %>%
#     pull(X3) %>%
#     qplot() +
#     theme_bw(base_size = 12, base_family = "Open Sans") +
#     labs(x = "Pair of successive trials", y = "Frequency") +
#     scale_y_continuous(breaks = 0:10, limits = c(0, 10) )

# Importing the lists of words for training
training_corpus <- read.csv("linguistic_material/training_corpus.csv") %>%
    select(hand, word)

# Importing the final lists of words (post-training)
final_corpus <- read.csv("linguistic_material/final_corpus.csv") %>%
    select(hand, word)

# Defining the (maximal) number of participants
nppt <- 70

# Defining the number of blocks
# NB : For each block, we have 8 reps of the 8 pairs of interest
nblocks <- 6

# Defining the number of trials per block
ntrials <- 65

for (i in 1:nppt) { # For each participant, populate sequences of pairs with appropriate words
    
    # Defining the name of participant
    participant <- paste0("S", sprintf(fmt = "%02d", i) )
    
    # Defining the output directory (i.e., where the csv files should be stored)
    output_dir <- paste0("randomisation/", participant, "/")
    
    # If it does not exist yet, creates a directory for this participant
    if (!dir.exists(output_dir) ) {dir.create(output_dir)}
    
    # Initialising an empty dataframe
    conditions <- data.frame(
        block = rep(x = 1:nblocks, each = ntrials),
        trial = rep(x = 1:ntrials, times = nblocks),
        sequence = numeric(length = nblocks * ntrials),
        hand = character(length = nblocks * ntrials),
        mode = character(length = nblocks * ntrials),
        word = character(length = nblocks * ntrials)
        )
    
    for (j in 1:nblocks) { # For each block
        
        # Generating a sequence of four stimuli, without stimulus repetition,
        # and with 4 repetitions
        experiment <- Euler(stimuli = 4, stim_repeat = "False", pair_repeats = 4)
        sequences <- as.numeric(experiment$get_sequence() ) + 1
        
        conditions <- conditions %>%
            mutate(sequence = ifelse(block == j, sequences, sequence) ) %>%
            mutate(
                hand = case_when(
                    sequence %in% c(1, 3) ~ "left",
                    sequence %in% c(2, 4) ~ "right"
                    )
                ) %>%
            mutate(
                mode = case_when(
                    sequence %in% c(1, 2) ~ "imagined",
                    sequence %in% c(3, 4) ~ "executed"
                    )
                )
        
        k <- 1
        
        while (k <= ntrials) { # For each trial in this block, populates with a word
            
            conditions[conditions$block == j, ]$word[k] <- ifelse(
                conditions[conditions$block == j, ]$sequence[k] %in% c(1, 3),
                final_corpus %>%
                    filter(hand == "left") %>%
                    sample_n(size = 1) %>%
                    pull(word),
                final_corpus %>%
                    filter(hand == "right") %>%
                    sample_n(size = 1) %>%
                    pull(word)
                )
            
            # Find sequences of words to check whether some words are repeated...
            
            repeated_words <- rle(
                conditions[conditions$block == j & conditions$trial <= k, ]$word
                )$lengths
            
            if (max(repeated_words) > 1) { # If a word is repeated, 
                
                # Picks another word for the current iteration
                invisible()
                
            } else {
                
                # If not, goes to next word
                k <- k + 1
                
            }
            
        }
        
        # Writes conditions file for this participant and this block
        write.csv(
            x = conditions[conditions$block == j, ] %>% select(word, hand, mode),
            file = paste0(output_dir, "block", sprintf(fmt = "%02d", j), "_conditions.csv"),
            quote = FALSE, row.names = FALSE
            )
        
    }
    
    # Writes blocks file for this participant
    write.csv(
        x = data.frame(
            participant_block = c(
                paste0(participant, "/block01_conditions.csv"),
                paste0(participant, "/block02_conditions.csv"),
                paste0(participant, "/block03_conditions.csv"),
                paste0(participant, "/block04_conditions.csv"),
                paste0(participant, "/block05_conditions.csv"),
                paste0(participant, "/block06_conditions.csv")
                )
            ),
        file = paste0(output_dir, "blocks.csv"),
        quote = FALSE, row.names = FALSE
        )
    
    # Writes training file(s) for this participant
    write.csv(
        x = training_corpus %>%
            sample_n(size = 33, replace = TRUE) %>%
            select(word, hand),
        file = paste0(output_dir, "training_executed.csv"),
        quote = FALSE, row.names = FALSE
        )
    
    # Writes training file(s) for this participant
    write.csv(
        x = training_corpus %>%
            sample_n(size = 33, replace = TRUE) %>%
            select(word, hand),
        file = paste0(output_dir, "training_imagined.csv"),
        quote = FALSE, row.names = FALSE
        )
    
    # Writes training file(s) for this participant
    write.csv(
        x = training_corpus %>%
            sample_n(size = ntrials, replace = TRUE) %>%
            select(word, hand) %>%
            mutate(
                mode = sample(
                    x = c("executed", "imagined"), size = ntrials, replace = TRUE)
                ),
        file = paste0(output_dir, "training_mixed.csv"),
        quote = FALSE, row.names = FALSE
        )
    
    # Prints progress
    cat("Participant done:", participant, "\n")
    
}

# Checking word frequencies across participants (they should be similar)
blocks <- list.files(path = "randomisation", pattern = "block0", full.names = TRUE, recursive = TRUE)
all_blocks <- read_csv(file = blocks, id = "filename")

all_blocks %>%
    data.frame %>%
    ggplot(aes(x = interaction(word, hand), fill = hand) ) +
    geom_bar(stat = "count", show.legend = FALSE) +
    theme_bw(base_size = 12, base_family = "Open Sans") +
    labs(x = "Word", y = "Frequency") +
    scale_fill_brewer(palette = "Dark2")
