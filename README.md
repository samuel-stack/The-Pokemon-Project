# Whats the Next Pokémon?

----
# Recommendation Process
How am I going to make recommendations?  I want to focus on Type pairings and recommend via those. I want to identify pairings that do not exist and calculate if they would be a balanced fit considering the distribution of others.

I want to identify pairings that are rare or do not exist and access how they would fit in to the current structure.  To do this I'm going to look at some summary stats that exist for all current pokémon and Identify ranges of these values that recommended type pairings must fall in in order for me to recommend them.

Heres my [medium post](https://medium.com/@sam.stack/whats-that-pok%C3%A9mon-8c838a02f3d8) walking through way too much of the backgroun information on pokémon then coming to the conclusions.

### Analysis Process

[Table Cleaning and Formatting](1-Pokemon_Table_formatting.ipynb)
- The Original Data I was working with need to be cleaned up a bit.

[Pokemon Table Creation](2-Poke-Table-Creation.ipynb)
- Creating 2 Pivot tables to represent type advantages and type-by-type listings.

[Barchart Investigation](3-Poke-Type-Barcharts.ipynb)
- Bart Charts to analyze which type-sets to note exist.

[Type Investigation I](4-Type-Investigation.ipynb)
- Initial Calculations for Existent Types for focus attributes given a type set.

[Type Investivation II](5-Type-Investigation-2.ipynb)
- Further Calculations for Non-Existent Types for focus attributes given a type set.

[Final Recommendations](6-Type-Recommendations.ipynb)
- Heatmaps to reveal final type sets to propose.

[Pokemon Heatmap](7-Poke-Heatmap.ipynb)
- Investigative heatmap to see if the info gained from several barcharts could be gained from a single heatmap.

----

# Background Information

### C-C-C-COMBO BREAKER!!!

Before we can go about making recommendations about type combinations, lets take a look at the results of combinations.  What I'm trying to say is, we don't want to recommend a type combination that is too powerful in that it can have an offensive of defensive advantage over all of most other types and essentially be an offensive and/or defensive juggernaut.

First, a brief explanation how damage is calculated.

**Attacking a Pokemon with 1 type**  
`Damage Multiplier * Base Damage`

**Attacking a Pokemon with 2 different Types**  
`(Damage Multiplier(type1) * Damage Multiplier(type2) * Base Damage`


Given this set up, in order to keep things balanced...
1. We do not want to propose a combination that has a offensive type advantage over all or most other types.
2. We do not want to propose a combination that has a defensive advantage over all or most other types AND does not have defensive immunity over many types.

Lets look at an example: A Pokemon that has both Fire and Water ([Volcanion](https://bulbapedia.bulbagarden.net/wiki/Volcanion_(Pok%C3%A9mon))).

### Offensive

**Advantage**
Volcanion can potentially utilize moves from the Fire and Water pools giving it the potential to have a "super-effective" offensive advantage over 7 of the 18 other types.     
    - Fire has a 2x advantage over Bug, Grass, Ice and Steel
    - Water has a x2 advantage over Fire, Ground and Rock.

**Disadvantage**   
    - There are no types that are completely immune to either Fire or Water


### Defensive

**Advantage**
    - The Fire and Water combo has no Immunities
    - Fire and Water combo has very good defense against Fire, Ice and Steel types (If GoT had types)

**Disadvantage**
    - Fire and Water combo has no significant weaknesses.
    - Electric and Ground have the most affect but only up to a x2 multiplier.


-----

### "Now thats just wrong."
The last consideration I am going to make when making type proposals is regarding if "Does this combo make sense."  Once again, I'll use Volcanion whose Fire/Water combo does NOT make sense as they are polar opposites. However, Volcanion is a legendary Pokemon so it can slide.  

Types that are just wrong.
- Fire & Water (Volcanion - _Legendary_)
- Fire & Grass
- Fire & Ice (George R.R. Martin - _Procrastinator_)
- Dragon & Fairy (Mega Alteria - _Mega Form_)
