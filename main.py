def draw_grid():
    for col in range(COLS):
        for row in range(ROWS):
            # Only set the Initial cell if we are NOT dragging
            if (grid[col, row] == INITIAL and not initial_cell_dragging):
                draw_cell(INITIAL_CELL_COLOR, col, row)
            # Only set the Terminal cell if we are NOT dragging
            elif (grid[col, row] == TERMINAL and not terminal_cell_dragging):
                draw_cell(TERMINAL_CELL_COLOR, col, row)
            elif (grid[col, row] == WALL):
                draw_cell(WALL_CELL_COLOR, col, row)
            elif (grid[col, row] == VISITED):
                draw_cell(VISITED_CELL_COLOR, col, row)
            elif (grid[col, row] == PATH):
                draw_cell(PATH_CELL_COLOR, col, row)
            else:  # (grid[col, row] == EMPTY)
                draw_cell(EMPTY_CELL_COLOR, col, row)

    if (initial_cell_dragging):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        cell_col = int(mouse_x / CELL_WIDTH)
        cell_row = int(mouse_y / CELL_HEIGHT)
        # Check the current mouse-pointer for the dragging
        # motion is actually on the board
        if (valid_cell(cell_col, cell_row)):
            draw_cell(INITIAL_CELL_COLOR,
                      cell_col,
                      cell_row)
    elif (terminal_cell_dragging):
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        cell_col = int(mouse_x / CELL_WIDTH)
        cell_row = int(mouse_y / CELL_HEIGHT)
        # Check the current mouse-pointer for the dragging motion
        # is actually on the board
        if (valid_cell(cell_col, cell_row)):
            draw_cell(TERMINAL_CELL_COLOR, cell_col, cell_row)
