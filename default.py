 # Main menu
45 def main_list(params):
46    plugintools.log("totalserver.main_list "+repr(params))
47
48    plugintools.add_item( 
49        action="disneyweb", 
50        title=plugintools.get_localized_string(T_OFFICIAL_WEBSITE) ,
51        url="http://www.disney.es/disney-junior/contenido/video.jsp" ,
52        folder=True )
53    
54    plugintools.add_item(
55        action="youtube_playlists",
56        title="Nadie Sabe Nada",
57        url="http://gdata.youtube.com/feeds/api/users/"+YOUTUBE_CHANNEL_ID+"/PLXrr3O2Jm9ffp0HNK-cBC97RFQFM8om9d",
58        folder=True )
59    
60    plugintools.add_item( action="search",
61        title=plugintools.get_localized_string(T_SEARCH) )
62    
63    plugintools.add_item( action="preferences",
64        title=plugintools.get_localized_string(T_PREFERENCES),
65        folder = False )