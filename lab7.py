from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    def test_youtube_homepage():
        driver.get("https://www.youtube.com/")
        assert "YouTube" in driver.title

    def test_search_video():
        driver.get("https://www.youtube.com/")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        search_box.send_keys("Selenium")
        search_box.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(
            EC.title_contains("Selenium")
        )
        assert "Selenium" in driver.title

    def test_play_first_video():
        driver.get("https://www.youtube.com/results?search_query=Selenium")
        
        first_video = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'video-title'))
        )
        first_video.click()
        
        video_player = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "video"))
        )
        
        is_playing = driver.execute_script("return arguments[0].currentTime > 0;", video_player)
        assert is_playing, "Video is not playing"

    test_youtube_homepage()
    test_search_video()
    test_play_first_video()

finally:
    driver.quit()
