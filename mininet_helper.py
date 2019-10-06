
# --------- python code ------------
"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""
import json
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    hostsList = []
    switchesList = []
    
    def build( self ):
        "Create custom topo."

        # create hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )
        h9 = self.addHost( 'h9' )
        h10 = self.addHost( 'h10' )

        # create switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )

        # link up switches
        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s4 )

        # link up hosts to switches
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s2 )
        self.addLink( h4, s2 )
        self.addLink( h5, s3 )
        self.addLink( h6, s3 )
        self.addLink( h7, s4 )
        self.addLink( h8, s4 )
        self.addLink( h9, s4 )
        self.addLink( h10, s4 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
# --------- python code ------------