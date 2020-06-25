# IBM - Data Science
# Tool for Data Science
# RStudio IDE

# Lab: Creating an Interactive Map in R 

## Installing libraries related to project
install.packages(c("shiny","leaflet"))

## Loading Libraries
library(shiny)
library(leaflet)

r_colors <- rgb(t(col2rgb(colors()) / 255))
names(r_colors) <- colors()

ui <- fluidPage(
  leafletOutput("mymap"),
  p(),
  actionButton("recalc", "New points"),
  p(),
  textOutput("coordinates")
)

server <- function(input, output, session){
  
  points <- eventReactive(input$recalc, {
      points = cbind(rnorm(10) * 2 + 13, rnorm(10) + 48)
      output$coordinates <- renderText ({
      points })
    return(points)
  }, 
  ignoreNULL = FALSE)
  observeEvent(input$Map_shape_click,{ # update the location selectInput on map clicks
    soutput$coordinates <- renderText({
      "You have selected this"
    })
  })
  output$mymap <- renderLeaflet({
    leaflet()
      addProviderTiles(
        providers$Stamen.TonerLite,
        options = providerTileOptions(noWrap = TRUE)
      )
      addMarkers(data = points())
  })
  }


shinyApp(ui, server)


## Somehow I am getting error > Listening on http://127.0.0.1:5130
#                             > Warning: Error in : $ operator is invalid for atomic vectors
