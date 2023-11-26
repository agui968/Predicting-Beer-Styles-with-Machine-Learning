import pandas as pd

#Process detailed in 02limpieza.ipynb
beer1=pd.read_csv('../data/raw/recipeData.csv')

#DELETING USELESS COLUMNS
beer1=beer1.drop(columns=(['BeerID','Size(L)', 'URL', 'OG', 'BoilSize', 'BoilGravity','Efficiency','MashThickness',
                           'PitchRate','PrimaryTemp','PrimingAmount','UserId','FG','SugarScale','PrimingMethod','BoilTime']))

#Removing null style beers from the df
beer1.dropna(subset=['Style','Name'],axis=0,inplace=True)

#Mapping styles to sort them out
longstyle_map={'Blonde Ale':'Pale Lager/Blonde Ale', 'British Golden Ale':'Pale Lager/Blonde Ale','Cream Ale':'Pale Lager/Blonde Ale','Holiday/Winter Special Spiced Beer':'Other','American IPA':'Pale Ale', 'Belgian Blond Ale':'Pale Lager/Blonde Ale',
               'American Pale Ale':'Pale Ale','Imperial IPA':'Pale Ale','Robust Porter':'Stout/Porter','Bohemian Pilsener':'Pale Lager/Blonde Ale','Saison':'Pale Ale',
               'Northern English Brown':'Brown Ale','English IPA':'Pale Ale','Traditional Bock':'Other','Premium American Lager':'Pale Lager/Blonde Ale',
               'Double IPA':'Pale Ale','Belgian Golden Strong Ale':'Strong Ale','Double IPA':'Pale Ale','Light American Lager':'Pale Lager/Blonde Ale',
               'German Pilsner (Pils)':'Pale Lager/Blonde Ale','American Brown Ale':'Brown Ale','Oatmeal Stout':'Stout/Porter', 'Specialty Beer':'Other',
               'American Amber Ale':'Pale Ale','Kölsch':'Pale Lager/Blonde Ale', 'Witbier':'Wheat','Weizen/Weissbier':'Wheat','Trappist Single':'Other',
               'Russian Imperial Stout':'Stout/Porter','Specialty IPA: Black IPA':'Other', 'Sweet Stout':'Stout/Porter', 'Strong Scotch Ale':'Strong Ale',
               'Belgian Tripel':'Pale Ale','American Stout':'Stout/Porter','Belgian Pale Ale':'Pale Ale','Dark American Lager':'Other', 'Dry Stout':'Stout/Porter',
               'Belgian Dark Strong Ale':'Strong Ale','American Wheat or Rye Beer':'Wheat','Vienna Lager':'Pale Lager/Blonde Ale','Special/Best/Premium Bitter':'Other',
               'Experimental Beer':'Other','Irish Red Ale':'Other', 'Old Ale':'Other','Altbier':'Other','Extra Special/Strong Bitter (ESB)':'Pale Ale',
               'Winter Seasonal Beer':'Other','Standard American Lager':'Pale Lager/Blonde Ale', 'Wood-Aged Beer':'Other','Fruit Beer':'Other', 'Golden Ale':'Pale Ale',
               'Flanders Red Ale':'Other','Berliner Weisse':'Wheat','Oktoberfest/Märzen':'Pale Lager/Blonde Ale','Munich Helles':'Pale Lager/Blonde Ale',
               'Classic American Pilsner':'Pale Lager/Blonde Ale','Gueuze':'Other','Brown Porter':'Stout/Porter','American Light Lager':'Pale Lager/Blonde Ale', 'English Cider':'Other',
               'Fruit Cider':'Other','Spice  Herb  or Vegetable Beer':'Other','Southern English Brown':'Brown Ale','Other Smoked Beer':'Other',
               'Belgian Dubbel':'Strong Ale','Cyser (Apple Melomel)':'Other','Metheglin':'Other','Specialty IPA: Red IPA':'Other', 'Belgian Specialty Ale':'Other',
               'Foreign Extra Stout':'Stout/Porter','Braggot':'Other','Weizenbock':'Other', 'International Pale Lager':'Pale Lager/Blonde Ale','Common Cider':'Other',
               'Imperial Stout':'Stout/Porter', 'Strong Bitter':'Pale Ale','Dusseldorf Altbier':'Other','Bière de Garde':'Other','Dunkelweizen':'Other',
               'Schwarzbier':'Stout/Porter','Baltic Porter':'Stout/Porter','Doppelbock':'Other','American Barleywine':'Strong Ale','Other Specialty Cider or Perry':'Other',
               'Specialty IPA: White IPA':'Other','Mild':'Other','California Common Beer':'Other','American Wheat Beer':'Wheat','British Strong Ale':'Strong Ale',
               'Other Fruit Melomel':'Other','Classic Rauchbier':'Other','Märzen':'Pale Lager/Blonde Ale','American Lager':'Pale Lager/Blonde Ale','Wee Heavy':'Strong Ale',
               'Dry Mead':'Other','British Brown Ale':'Brown Ale', 'Weissbier':'Wheat','Clone Beer':'Other','Best Bitter':'Pale Ale','Standard/Ordinary Bitter':'Pale Ale',
               'Czech Premium Pale Lager':'Pale Lager/Blonde Ale','Mixed-Fermentation Sour Beer':'Other','Scottish Heavy 70/-':'Other','English Porter':'Stout/Porter',
               'Czech Dark Lager':'Other', 'Roggenbier (German Rye Beer)':'Other','Gose':'Other','Fruit Lambic':'Other','Sweet Mead':'Other','Australian Sparkling Ale':'Other',
               'Maibock/Helles Bock':'Other','American Strong Ale':'Strong Ale','Specialty IPA: Belgian IPA':'Pale Ale','Mixed-Style Beer':'Other','North German Altbier':'Other',
               'American Porter':'Stout/Porter','Dortmunder Export':'Pale Lager/Blonde Ale','German Pils':'Pale Lager/Blonde Ale','Irish Stout':'Stout/Porter','English Barleywine':'Strong Ale',
               'Specialty IPA: Rye IPA':'Other','Scottish Export':'Strong Ale','Scottish Export 80/-':'Other','Tropical Stout':'Stout/Porter','Eisbock':'Other',
               'Semi-Sweet Mead':'Other','French Cider':'Other','Munich Dunkel':'Other','Specialty Smoked Beer':'Other','Open Category Mead':'Other',
               'Wild Specialty Beer':'Other','Apple Wine':'Other','Czech Pale Lager':'Pale Lager/Blonde Ale','California Common':'Other','Flanders Brown Ale/Oud Bruin':'Other',
               'International Amber Lager':'Other','Alternative Grain Beer':'Other','Scottish Light 60/-':'Other','Helles Bock':'Other','Lambic':'Other', 'Pre-Prohibition Lager':'Other',
               'Ordinary Bitter':'Pale Ale','Wheatwine':'Other','Dunkles Weissbier':'Other','Straight (Unblended) Lambic':'Other','Kentucky Common':'Other','New England Cider':'Other',
               'Pyment (Grape Melomel)':'Other','Lichtenhainer':'Other','Irish Extra Stout':'Stout/Porter','Rauchbier':'Other','Specialty IPA: Brown IPA':'Other',
               'Kellerbier: Amber Kellerbier':'Pale Lager/Blonde Ale','Sahti':'Other','Oud Bruin':'Other','Piwo Grodziskie':'Other','Specialty Fruit Beer':'Other','Alternative Sugar Beer':'Other',
               'Kellerbier: Pale Kellerbier':'Pale Lager/Blonde Ale','Classic Style Smoked Beer':'Other','Czech Amber Lager':'Other','Scottish Heavy':'Other','Traditional Perry':'Other',
               'Festbier':'Pale Lager/Blonde Ale','Brett Beer':'Other','Dark Mild':'Other','London Brown Ale':'Brown Ale','Fruit and Spice Beer':'Other', 'German Helles Exportbier':'Pale Lager/Blonde Ale',
               'Autumn Seasonal Beer':'Other','International Dark Lager':'Other','Roggenbier':'Other','Dunkles Bock':'Other','German Leichtbier':'Pale Lager/Blonde Ale',
               'Scottish Light':'Other','Pre-Prohibition Porter':'Other','Specialty Wood-Aged Beer':'Other'

} #remove Other;
beer1['Simple_style']=beer1['Style'].map(longstyle_map)
#Remove 'Other' style
beer1=beer1.drop(beer1[beer1['Simple_style']=='Other'].index)

#Create new column with new style codes (ordered by color)
style_map_color = {
    "Wheat": 0,
    "Pale Lager/Blonde Ale": 1,
    "Pale Ale": 2,
    "Strong Ale": 3,
    "Brown Ale": 4,
    "Stout/Porter":5
}
beer1['Style_color'] = beer1['Simple_style'].map(style_map_color)
beer1.head()

# style_map_ibu = { #ORDERED BY IBU
#     "Wheat": 0,
#     "Pale Lager/Blonde Ale": 1,
#     "Brown Ale": 2,
#     "Strong Ale": 3,
#     "Stout/Porter":4,
#     "Pale Ale":5
# }
# beer1['Style_ibu'] = beer1['Simple_style'].map(style_map_ibu)
#Save the new csv
# beer1.to_csv('..\\data\\processed\\clean_styles_mapped.csv')

#Process detailed in 03limpieza_EDA.ipynb
beer=pd.read_csv('../data/processed/clean_styles_mapped.csv',index_col=0)

# Remove duplicates and correct outliers / wrong values
beer=beer.drop_duplicates(subset='Name')
beer.loc[(beer['Simple_style'] == 'Pale Lager/Blonde Ale') & (beer['Color'] > 6), 'Color'] = 6
beer.loc[(beer['Simple_style'] == 'Pale Lager/Blonde Ale') & (beer['IBU'] > 28), 'IBU'] = 28

beer = beer[beer['ABV'] != 54.72]
beer = beer[(beer['ABV'] != 0.0) & (beer['IBU'] != 0.0) & (beer['Color'] != 0.0)]
beer.loc[(beer['Simple_style'] == 'Strong Ale') & (beer['ABV'] < 6), 'ABV'] = 6
beer.loc[(beer['Simple_style'] == 'Pale Lager/Blonde Ale') & (beer['ABV'] > 6.5), 'ABV'] = 6.4

beer.loc[(beer['Simple_style'] == 'Pale Ale') & (beer['Color'] > 15), 'Color'] = 15
beer.loc[(beer['Simple_style'] == 'Pale Ale') & (beer['Color'] < 5), 'Color'] = 5
beer.loc[(beer['Simple_style'] == 'Wheat') & (beer['Color'] > 6), 'Color'] = 6
beer.loc[(beer['Simple_style'] == 'Strong Ale') & (beer['Color'] > 22), 'Color'] = 22
beer.loc[(beer['Simple_style'] == 'Brown Ale') & (beer['Color'] < 12), 'Color'] = 12
beer.loc[(beer['Simple_style'] == 'Stout/Porter') & (beer['Color'] < 17), 'Color'] = 17

beer.loc[(beer['Simple_style'] == 'Pale Ale') & (beer['IBU'] > 100), 'IBU'] = 90
beer.loc[(beer['Simple_style'] == 'Stout/Porter') & (beer['IBU'] > 90), 'IBU'] = 90
beer.loc[(beer['Simple_style'] == 'Stout/Porter') & (beer['IBU'] < 18), 'IBU'] = 18
beer.loc[(beer['Simple_style'] == 'Strong Ale') & (beer['IBU'] < 20), 'IBU'] = 20
beer.loc[(beer['Simple_style'] == 'Strong Ale') & (beer['IBU'] > 100), 'IBU'] = 100
beer.loc[(beer['Simple_style'] == 'Wheat') & (beer['IBU'] > 30), 'IBU'] = 30
beer.loc[(beer['Simple_style'] == 'Pale Lager/Blonde Ale') & (beer['IBU'] < 8), 'IBU'] = 8
beer.loc[(beer['Simple_style'] == 'Pale Ale') & (beer['IBU'] < 30), 'IBU'] = 30

beer.reset_index(drop=True, inplace=True)
#Save the new csv
# beer.to_csv('../data/processed/clean_limited.csv')