require_relative "lib/crawlora/modrinth/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-modrinth"
  spec.version = Crawlora::Modrinth::VERSION
  spec.summary = "Modrinth API client for Crawlora (34 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Modrinth API. Covers project search and metadata, versions, dependencies, collections, organizations, and file compatibility across 34 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=modrinth-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-modrinth", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-modrinth/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
