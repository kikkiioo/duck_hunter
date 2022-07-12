classDiagram
    Actors<|--Duck
    Actors<|-- Dog
    Actors<|--Player
    Duck<|--RedDuck
    Duck<|--BlueDuck
    Duck<|--BlackDuck
    Game --o UIWindow
    Game o-- Actors
    ActorsController o--DuckController
    ActorsController o-- DogController
    ActorsController o-- PlayerController
    Game *-- GameController

    %% view 
    class UIWindow{
        game:Game
        opponent: Dict[opponent_type, List [png]]
        opponent_score: Dict[opponent_type, duck_score]
        opponent_being_shot: Dict[opponent_type,List[png]]
        dog: Dict[dog_animation, List[png]]

        start_main_loop()
        capture_keyboard_inputs()

    }

    class Game{
    Level: Int
    Score: Int
    ShotCount: Int
    
    displayBackground()
    displayScore()
    displayHitDucks()
    displayHitLine()
    displayShot()
    displayLevel()
    displayDuckScore()

  }

    %% model - data

    class Actors{
      Xpos: Double
      Ypos: Double
    }
    
    class Duck{
      flyingSpeed: Double
      endXpos: Double
      endYpos: Double
     
    }
    class Dog{       
      
    }
    class RedDuck{
    redScore: Int
    }
  class BlueDuck{
    blueScore: Int
    }
  class BlackDuck{
    blackScore: Int
    }

  class Player{
    shotCount: Int
    hitCount: Int
    successShotCount: Int
  }
    
    %% controllers

    class PlayerController{
      shoot()
      missShot()
      successShot()
    }

    class GameController{
      startGame()
      createDuck()
      nextLevel()
      updateScore()
      updateLevel()
      updateShot()
      updateHitCount()
      updateHitLine()
      updateDuckSpeed()
      updateDuckScore()
      isGameOver()
      isnextLevel()
      gameOver() 
    }

    class ActorsController{
      execute_move(Actors: actor)
    }

    class DuckController{
      quack()
      fly()
      updateXendPos()
      updateYendPos()
      isDead()
      flewAway()
      beingShot()
    }
    class DogController{
        catchDuck()
        sniff()
        jump()
        giggle()
        bark()
    }