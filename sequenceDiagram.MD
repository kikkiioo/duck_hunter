sequenceDiagram

    participant gameController
    participant UIWindow
    participant Game
    participant playerController   
    participant actorController
    participant dogController

    
    gameController->>gameController: startGame()
    gameController->>UIWindow: start_main_loop()
    
    loop break when game over
    
    gameController-->>actorController: execute_move()
    actorController-->>dogController: 
    dogController-->>dogController: sniff() and jump() 
    loop break when hit count max or game over
    
    gameController-->>gameController: createDuck()
    gameController-->>actorController: execute_move()
    actorController-->>duckController: 
    duckController-->>duckController: fly()
    
    loop break when shot duck or missed shot (three times)
    gameController-->>actorController: execute_move()
    actorController-->>playerController: 
    playerController-->>playerController: shoot()
    gameController-->>actorController: execute_move()
    actorController-->>duckController: 
    duckController-->>duckController:isDead()
    duckController-->>duckController:updateXendPos() and updateYendPos()
    gameController->>gameController: updateShot()
    end
    
    gameController-->>actorController: execute_move()
    actorController-->>dogController: 
    dogController-->>dogController: giggle() if missed shot

    gameController-->>actorController: execute_move()
    actorController-->>duckController: 
    duckController-->>duckController: flewAway() or beingShot()

    gameController-->>gameController: displayDuckScore()

    gameController->>gameController: updateScore()
    gameController->>gameController: updateHitCount()
    gameController->>gameController: updateShot()

    gameController-->>actorController: execute_move()
    actorController-->>dogController: 
    dogController-->>dogController: catchDuck()

    gameController->>gameController: isGameOver()
    gameController->>gameController: isnextLevel() 
    
    end

    gameController->>gameController: updateLevel()

    end
    gameController-->>actorController: execute_move()
    actorController-->>dogController: 
    dogController-->>dogController: giggle() 
    gameController->>gameController: gameover()

            