##  Now that we know that our customers love rock music, we can decide which musicians to 
##  invite to play at the concert. 

##  Let's invite the artists who have written the most rock music in our dataset.
##  Write a query that returns the Artist name and total track count of the top 10 rock bands. 


QUERY ='''
SELECT Artist.Name as Artist, COUNT(Track.TrackId) as Count FROM Artist 
JOIN Album ON Artist.ArtistId = Album.ArtistId
JOIN Track ON Album.AlbumId = Track.AlbumId
JOIN Genre ON Track.GenreId = Genre.GenreId
WHERE Genre.Name = 'Rock' 
GROUP BY Artist.Name
ORDER BY COUNT(Track.TrackId) desc
LIMIT 10;


'''

'''
---Visual Guide---

Before Query...

#############      #############      #############      ############
#    Genre  #      #   Track   #      #   Album   #      #  Artist  #
#############      #############      #############      ############
|  GenreId  | ---> |  GenreId  |      |  ArtistId  | --->| ArtistId |
+-----------+      +-----------+      +-----------+      +----------+
|  Name     |      |  AlbumId   |---> |  AlbumId  |      |  Name    |
+-----------+      +-----------+      +-----------+      +----------+

After Query...

#######################################
#             GenreArtist             #
#######################################
|  Artist.Name  |  COUNT(Genre.Name)  |
+---------------+---------------------+

'''