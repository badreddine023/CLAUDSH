import { useAuth } from "@/_core/hooks/useAuth";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { ArrowRight, BookOpen, Brain, Zap, Globe, BarChart3, Network } from "lucide-react";
import { getLoginUrl } from "@/const";

export default function Home() {
  const { user, loading, isAuthenticated, logout } = useAuth();

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-950 dark:to-slate-900">
      {/* Navigation */}
      <nav className="sticky top-0 z-50 bg-white/80 dark:bg-slate-950/80 backdrop-blur-sm border-b border-slate-200 dark:border-slate-800">
        <div className="container mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <BookOpen className="w-6 h-6 text-blue-600" />
            <h1 className="text-2xl font-bold text-slate-900 dark:text-white">CLAUDSH</h1>
          </div>
          <div className="flex items-center gap-4">
            {isAuthenticated ? (
              <>
                <span className="text-sm text-slate-600 dark:text-slate-300">{user?.name}</span>
                <Button variant="outline" onClick={logout}>
                  Logout
                </Button>
              </>
            ) : (
              <Button onClick={() => window.location.href = getLoginUrl()}>
                Login
              </Button>
            )}
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="container mx-auto px-4 py-20">
        <div className="max-w-4xl mx-auto text-center">
          <Badge className="mb-4 bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-100">
            Quranic Hyper-Analysis Framework
          </Badge>
          <h2 className="text-5xl font-bold mb-6 text-slate-900 dark:text-white">
            Transform the Quran into a Multi-Dimensional Information Space
          </h2>
          <p className="text-xl text-slate-600 dark:text-slate-300 mb-8">
            Combining classical Islamic scholarship with modern computational linguistics to reveal hidden patterns, word relationships, and semantic networks within the sacred text.
          </p>
          <div className="flex gap-4 justify-center">
            <Button size="lg" className="bg-blue-600 hover:bg-blue-700">
              Explore Analysis <ArrowRight className="ml-2 w-4 h-4" />
            </Button>
            <Button size="lg" variant="outline">
              Learn More
            </Button>
          </div>
        </div>
      </section>

      {/* Core Objectives */}
      <section className="container mx-auto px-4 py-16">
        <h3 className="text-3xl font-bold mb-12 text-center text-slate-900 dark:text-white">
          Core Objectives
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            {
              icon: Brain,
              title: "Linguistic Analysis",
              description: "Extract Arabic morphological structures and semantic relationships"
            },
            {
              icon: BarChart3,
              title: "Mathematical Modeling",
              description: "Apply statistical analysis and pattern recognition"
            },
            {
              icon: Globe,
              title: "Bilingual Integration",
              description: "Maintain parallel Arabic and English analysis"
            },
            {
              icon: Network,
              title: "Semantic Discovery",
              description: "Find precise meanings through contextual analysis"
            }
          ].map((objective, idx) => (
            <Card key={idx} className="p-6 hover:shadow-lg transition-shadow">
              <objective.icon className="w-8 h-8 text-blue-600 mb-4" />
              <h4 className="font-semibold text-lg mb-2 text-slate-900 dark:text-white">
                {objective.title}
              </h4>
              <p className="text-slate-600 dark:text-slate-400">
                {objective.description}
              </p>
            </Card>
          ))}
        </div>
      </section>

      {/* Roadmap Phases */}
      <section className="container mx-auto px-4 py-16 bg-white dark:bg-slate-900 rounded-lg my-12">
        <h3 className="text-3xl font-bold mb-12 text-center text-slate-900 dark:text-white">
          Development Roadmap
        </h3>
        <div className="space-y-8">
          {[
            {
              phase: "Phase 1",
              title: "Data Preparation",
              status: "In Progress",
              items: [
                "Load Quran text with metadata",
                "Normalize Arabic text",
                "Extract morphological roots",
                "Tag POS and grammatical roles"
              ]
            },
            {
              phase: "Phase 2",
              title: "Core Analysis Modules",
              status: "In Progress",
              items: [
                "Implement Markov chain analysis (1st-5th order)",
                "Calculate transition probability matrices",
                "Shannon entropy calculations",
                "KL divergence analysis"
              ]
            },
            {
              phase: "Phase 3",
              title: "Local/Non-Local Duality",
              status: "Planned",
              items: [
                "Glocality score calculation",
                "Local cohesion metrics",
                "Global connectedness analysis",
                "Surah ranking by glocality"
              ]
            },
            {
              phase: "Phase 4",
              title: "Semantic Field Analysis",
              status: "Planned",
              items: [
                "Thematic clustering (10-15 clusters)",
                "Co-occurrence matrix building",
                "Theme transition probabilities",
                "Semantic Markov chains"
              ]
            },
            {
              phase: "Phase 5",
              title: "Visualization & Dashboard",
              status: "Planned",
              items: [
                "Interactive network graphs",
                "Heatmap matrices",
                "Markov state diagrams",
                "Real-time analysis dashboards"
              ]
            },
            {
              phase: "Phase 6",
              title: "AI Integration",
              status: "Planned",
              items: [
                "LLM-powered meaning discovery",
                "Semantic understanding",
                "Contextual recommendations",
                "Intelligent search"
              ]
            }
          ].map((roadmap, idx) => (
            <div key={idx} className="border-l-4 border-blue-600 pl-6 pb-6">
              <div className="flex items-center gap-3 mb-3">
                <Badge variant={roadmap.status === "In Progress" ? "default" : "secondary"}>
                  {roadmap.status}
                </Badge>
                <h4 className="text-2xl font-bold text-slate-900 dark:text-white">
                  {roadmap.phase}: {roadmap.title}
                </h4>
              </div>
              <ul className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {roadmap.items.map((item, itemIdx) => (
                  <li key={itemIdx} className="flex items-start gap-2 text-slate-600 dark:text-slate-400">
                    <Zap className="w-4 h-4 text-blue-600 mt-1 flex-shrink-0" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </section>

      {/* Analysis Layers */}
      <section className="container mx-auto px-4 py-16">
        <h3 className="text-3xl font-bold mb-12 text-center text-slate-900 dark:text-white">
          Analysis Layers
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {[
            {
              title: "Local Dimension (Micro-Structure)",
              items: [
                "Word-level frequency distributions per surah",
                "N-gram Markov chains (1st to 5th order)",
                "Intra-verse semantic networks",
                "Morphological root transitions",
                "Rhythmic/prosodic patterns"
              ]
            },
            {
              title: "Non-Local Dimension (Macro-Structure)",
              items: [
                "Cross-chapter thematic recurrence",
                "Inter-surah word distribution distances",
                "Revelation sequence vs. canonical order",
                "Hapax legomena distribution",
                "Topological concept networks"
              ]
            },
            {
              title: "Information-Theoretic Metrics",
              items: [
                "Shannon entropy per surah",
                "Relative entropy (KL divergence)",
                "Markov chain stationarity analysis",
                "Redundancy quantification",
                "Information density mapping"
              ]
            },
            {
              title: "Semantic Extraction",
              items: [
                "Co-occurrence matrix of roots",
                "Contextual meaning vectors",
                "Syntactic role tagging",
                "Thematic field proximity mapping",
                "Classical tafsir integration"
              ]
            }
          ].map((layer, idx) => (
            <Card key={idx} className="p-6">
              <h4 className="text-xl font-bold mb-4 text-slate-900 dark:text-white">
                {layer.title}
              </h4>
              <ul className="space-y-2">
                {layer.items.map((item, itemIdx) => (
                  <li key={itemIdx} className="flex items-start gap-2 text-slate-600 dark:text-slate-400">
                    <span className="text-blue-600 font-bold">•</span>
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </Card>
          ))}
        </div>
      </section>

      {/* Key Features */}
      <section className="container mx-auto px-4 py-16 bg-blue-50 dark:bg-blue-950/30 rounded-lg">
        <h3 className="text-3xl font-bold mb-12 text-center text-slate-900 dark:text-white">
          Key Features
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {[
            {
              title: "Comprehensive Database",
              description: "Word/root-level statistics with Markov probabilities for the entire Quranic corpus"
            },
            {
              title: "Advanced API",
              description: "Query local/non-local relationships and semantic networks programmatically"
            },
            {
              title: "Interactive Dashboard",
              description: "Toggle between verse-level, cross-Quran, and topological views"
            },
            {
              title: "Scholarly Reports",
              description: "Detailed analysis of information-theoretic patterns and discoveries"
            },
            {
              title: "Multilingual Support",
              description: "Arabic, English, and French documentation and analysis outputs"
            },
            {
              title: "Visualization Suite",
              description: "3D networks, heatmaps, Markov diagrams, and comparative charts"
            }
          ].map((feature, idx) => (
            <div key={idx} className="text-center">
              <h4 className="font-bold text-lg mb-2 text-slate-900 dark:text-white">
                {feature.title}
              </h4>
              <p className="text-slate-600 dark:text-slate-400">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </section>

      {/* CTA Section */}
      <section className="container mx-auto px-4 py-20 text-center">
        <h3 className="text-3xl font-bold mb-6 text-slate-900 dark:text-white">
          Ready to Explore?
        </h3>
        <p className="text-xl text-slate-600 dark:text-slate-300 mb-8 max-w-2xl mx-auto">
          Start analyzing the Quran with our advanced computational framework. Discover patterns invisible to linear reading.
        </p>
        <Button size="lg" className="bg-blue-600 hover:bg-blue-700">
          Begin Analysis <ArrowRight className="ml-2 w-4 h-4" />
        </Button>
      </section>

      {/* Footer */}
      <footer className="bg-slate-900 dark:bg-slate-950 text-white py-12 mt-20">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
            <div>
              <h4 className="font-bold mb-4">About</h4>
              <p className="text-slate-400 text-sm">Quranic Linguistic & Mathematical Analysis System</p>
            </div>
            <div>
              <h4 className="font-bold mb-4">Documentation</h4>
              <ul className="space-y-2 text-sm text-slate-400">
                <li><a href="#" className="hover:text-white">API Docs</a></li>
                <li><a href="#" className="hover:text-white">User Guide</a></li>
                <li><a href="#" className="hover:text-white">Examples</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold mb-4">Community</h4>
              <ul className="space-y-2 text-sm text-slate-400">
                <li><a href="#" className="hover:text-white">GitHub</a></li>
                <li><a href="#" className="hover:text-white">Issues</a></li>
                <li><a href="#" className="hover:text-white">Discussions</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold mb-4">Resources</h4>
              <ul className="space-y-2 text-sm text-slate-400">
                <li><a href="#" className="hover:text-white">Blog</a></li>
                <li><a href="#" className="hover:text-white">Research</a></li>
                <li><a href="#" className="hover:text-white">Contact</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-slate-800 pt-8 text-center text-slate-400 text-sm">
            <p>&copy; 2025 CLAUDSH - Quranic Hyper-Analysis Framework. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
