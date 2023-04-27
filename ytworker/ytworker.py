import seaborn as sns
import pandas as pd
from googleapiclient.discovery import build
import warnings
from config.config import configuration
import logging
import datetime

warnings.filterwarnings('ignore')
_yt_logger_ = logging.getLogger("youtube")

apiKey = configuration.get_property("apiKey")
youtube = build('youtube','v3',developerKey=apiKey)

# function to get youtube channel statistics.
def getChannelStats(channelID):
  dataframe = []
  request = request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=channelID,
    )
  response  = request.execute()
  try:
      for i in range(len(response['items'])):
          data = dict(
          ChannelName = response['items'][i]['snippet']['title'],
          Subscribers = response['items'][i]['statistics']['subscriberCount'],
          Views = response['items'][i]['statistics']['viewCount'],
          Videos = response['items'][i]['statistics']['videoCount'],
          PlaylistID = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'],
          # ChannelID = response['items'][i]['id'],
          Description = response['items'][i]['snippet']['description']
          )
          dataframe.append(data)
      return dataframe
  except Exception as e:
        return f'Some error occured due to {e}'

# function to get a specific channel's video IDs.
def getVideoIDs(playlistid):
  request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlistid,
        maxResults = 50
    )
  response = request.execute()
  videoids = []
  for i in range(len(response['items'])):
        videoids.append(response['items'][i]['contentDetails']['videoId'])

  nextpagetoken = response.get('nextPageToken')
  morepages = True
  while morepages:
    if nextpagetoken is None:
      morepages = False
    else:
      request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlistid,
        maxResults = 50,
        pageToken=nextpagetoken
      )
      response = request.execute()
      for i in range(len(response['items'])):
        videoids.append(response['items'][i]['contentDetails']['videoId'])

      nextpagetoken = response.get('nextPageToken')

  return videoids

# function to get a specific channel's video details based on video ID.
def getVideoDetails(videIDs):
    videoStats = []
    for i in range(0,len(videIDs),50):
        request = youtube.videos().list(
            part = 'snippet,statistics',
            id = ','.join(videIDs[i:i+50])
        )
        response = request.execute()
        try:
          for video in response['items']:
              videoinfo = dict(
                  Title = video['snippet']['title'],
                  PublishedDate = pd.to_datetime(video['snippet']['publishedAt']).strftime("%d-%m-%Y"),
                  ViewCount = video['statistics']['viewCount'],
                  LikeCount = video['statistics']['likeCount'],
                  CommentCount = video['statistics']['commentCount']
              )
              videoStats.append(videoinfo)
        except Exception as e:
           videoinfo = dict(
                  Title = video['snippet']['title'],
                  PublishedDate = pd.to_datetime(video['snippet']['publishedAt']).strftime("%d-%m-%Y"),
                  ViewCount = video['statistics']['viewCount'],
                  LikeCount = "No Like Data found.",
                  CommentCount = "No Comment Data found."
              )
        videoStats.append(videoinfo)
    return videoStats
