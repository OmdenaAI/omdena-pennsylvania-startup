import streamlit as st
import streamlit.components.v1 as components

def app():
    
    st.title("TradingView")
    #url = "https://public.tableau.com/views/TradingViewWorkbook/TRADINGVIEW?:language=en-US&:display_count=n&:origin=viz_share_link"
    #components.iframe(url,height = 1000,width = 1200)
    html_js = """
    <div class='tableauPlaceholder' id='viz1627456064438' style='position: relative'><noscript><a href='#'>    <img alt='TRADINGVIEW ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tr&#47;TradingViewWorkbook&#47;TRADINGVIEW&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
    <param name='embed_code_version' value='3' /> 
    <param name='site_root' value='' />
    <param name='name' value='TradingViewWorkbook&#47;TRADINGVIEW' />
    <param name='tabs' value='no' />
    <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tr&#47;TradingViewWorkbook&#47;TRADINGVIEW&#47;1.png' /> 
    <param name='animate_transition' value='yes' />
    <param name='display_static_image' value='yes' />
    <param name='display_spinner' value='yes' />
    <param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' />
    <param name='language' value='en-US' /></object></div>  
    <script type='text/javascript'>                    
    var divElement = document.getElementById('viz1627456064438');                    
    var vizElement = divElement.getElementsByTagName('object')[0];                    
    vizElement.style.width='1016px';vizElement.style.height='991px';                    
    var scriptElement = document.createElement('script');                    
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
    vizElement.parentNode.insertBefore(scriptElement, vizElement);                
    </script>'
    """

    components.html(html_js,height = 1000,width = 1100)