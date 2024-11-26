# generated by datamodel-codegen:
#   filename:  application.yml
#   timestamp: 2024-03-13T10:49:52+00:00

from __future__ import annotations

from typing import List, Optional, Dict, Union

from pydantic import BaseModel, Field, ConfigDict


class Parent(BaseModel):
    model_config = ConfigDict(extra='forbid')


class Whitelabel(Parent):
    enabled: Optional[bool] = None


class Error(Parent):
    whitelabel: Optional[Whitelabel] = None


class ServerServlet(Parent):
    context_path: Optional[str] = Field(None, alias='context-path')


class Server(Parent):
    port: Optional[int] = None
    error: Optional[Error] = None
    servlet: Optional[ServerServlet] = None


class SpringProfiles(Parent):
    active: Optional[str] = None


class MVCServlet(Parent):
    path: Optional[str] = None


class Mvc(Parent):
    servlet: Optional[MVCServlet] = None


class Main(Parent):
    banner_mode: Optional[str] = Field(None, alias='banner-mode')


class Spring(Parent):
    profiles: Optional[SpringProfiles] = None
    mvc: Optional[Mvc] = None
    main: Optional[Main] = None


class SyntaxHighlight(Parent):
    activated: Optional[bool] = None


class SwaggerUi(Parent):
    enabled: Optional[bool] = None
    path: Optional[str] = None
    tryItOutEnabled: Optional[bool] = None
    filter: Optional[bool] = None
    syntaxHighlight: Optional[SyntaxHighlight] = None
    showExtensions: Optional[bool] = None


class ApiDocs(Parent):
    path: Optional[str] = None
    version: Optional[str] = None


class Springdoc(Parent):
    swagger_ui: Optional[SwaggerUi] = Field(None, alias='swagger-ui')
    api_docs: Optional[ApiDocs] = Field(None, alias='api-docs')
    packages_to_scan: Optional[str] = Field(None, alias='packages-to-scan')
    pathsToMatch: Optional[str] = None


class File(Parent):
    name: Optional[str] = None


class Pattern(Parent):
    console: Optional[str] = None
    file: Optional[str] = None


class Org(Parent):
    heigit: Optional[str] = None


class Level(Parent):
    root: Optional[str] = None
    org: Optional[Org] = None


class Logging(Parent):
    file: Optional[File] = None
    pattern: Optional[Pattern] = None
    level: Optional[Level] = None


class Cors(Parent):
    allowed_origins: Optional[str] = None
    allowed_headers: Optional[str] = None
    preflight_max_age: Optional[int] = None


class Routing(Parent):
    enabled: Optional[bool] = None
    attribution: Optional[str] = None
    gpx_name: Optional[str] = None
    gpx_description: Optional[str] = None
    gpx_base_url: Optional[str] = None
    gpx_support_mail: Optional[str] = None
    gpx_author: Optional[str] = None
    gpx_content_licence: Optional[str] = None
    maximum_avoid_polygon_area: Optional[int] = None
    maximum_avoid_polygon_extent: Optional[int] = None
    maximum_alternative_routes: Optional[int] = None


class Matrix(Parent):
    enabled: Optional[bool] = None
    attribution: Optional[str] = None
    maximum_routes: Optional[int] = None
    maximum_routes_flexible: Optional[int] = None
    maximum_visited_nodes: Optional[int] = None
    maximum_search_radius: Optional[int] = None
    u_turn_costs: Optional[int] = None


class MaximumRangeDistanceItem(Parent):
    profiles: Optional[str] = None
    value: Optional[int] = None


class MaximumRangeTimeItem(MaximumRangeDistanceItem):
    pass


class Fastisochrones(Parent):
    maximum_range_distance_default: Optional[int] = None
    maximum_range_distance: Optional[List[MaximumRangeDistanceItem]] = None
    maximum_range_time_default: Optional[int] = None
    maximum_range_time: Optional[List[MaximumRangeTimeItem]] = None


class ProviderParameters(Parent):
    host: Optional[str] = None
    port: Optional[int] = None
    user: Optional[str] = None
    password: Optional[str] = None
    db_name: Optional[str] = None
    table_name: Optional[str] = None
    geometry_column: Optional[str] = None
    postgis_version: Optional[str] = None


class StatisticsProvider(Parent):
    enabled: Optional[bool] = None
    attribution: Optional[str] = None
    provider_name: Optional[str] = None
    property_mapping: Optional[Dict[str, str]] = None
    provider_parameters: Optional[ProviderParameters] = None


class Isochrones(Parent):
    enabled: Optional[bool] = None
    attribution: Optional[str] = None
    maximum_locations: Optional[int] = None
    maximum_intervals: Optional[int] = None
    allow_compute_area: Optional[bool] = None
    maximum_range_distance_default: Optional[int] = None
    maximum_range_distance: Optional[List[MaximumRangeDistanceItem]] = None
    maximum_range_time_default: Optional[int] = None
    maximum_range_time: Optional[List[MaximumRangeTimeItem]] = None
    fastisochrones: Optional[Fastisochrones] = None
    statistics_providers: Optional[Dict[str, StatisticsProvider]] = None


class Snap(Parent):
    enabled: Optional[bool] = None
    attribution: Optional[str] = None


class Endpoints(Parent):
    routing: Optional[Routing] = None
    matrix: Optional[Matrix] = None
    isochrones: Optional[Isochrones] = None
    Snap: Optional[Union[Snap, Dict]] = None  # using Union[Snap, Dict] to workaround Error:
    # ors.endpoints.Snap Input should be None


class Elevation(Parent):
    preprocessed: Optional[bool] = None
    data_access: Optional[str] = None
    cache_clear: Optional[bool] = None
    provider: Optional[str] = None
    cache_path: Optional[str] = None


class ExecEntry(Parent):
    active_landmarks: Optional[int] = None


class ExecAstarEntry(Parent):
    approximation: Optional[str] = None
    epsilon: Optional[float] = None


class ExecMethods(Parent):
    lm: Optional[ExecEntry] = None
    core: Optional[ExecEntry] = None
    astar: Optional[ExecAstarEntry] = None


class Execution(Parent):
    methods: Optional[ExecMethods] = None


class EncoderOptions(Parent):
    turn_costs: Optional[bool] = None
    block_fords: Optional[bool] = None
    use_acceleration: Optional[bool] = None
    maximum_grade_level: Optional[int] = None
    conditional_access: Optional[bool] = None
    conditional_speed: Optional[bool] = None
    consider_elevation: Optional[bool] = None

class PrepCH(Parent):
    enabled: Optional[bool] = None
    threads: Optional[int] = None
    weightings: Optional[str] = None


class PrepLM(PrepCH):
    landmarks: Optional[int] = None


class PrepCORE(PrepLM):
    lmsets: Optional[str] = None


class PrepFastIso(PrepCH):
    maxcellnodes: Optional[int] = None


class PrepMethods(Parent):
    lm: Optional[PrepLM] = None
    ch: Optional[PrepCH] = None
    core: Optional[PrepCORE] = None
    fastisochrones: Optional[PrepFastIso] = None


class Preparation(Parent):
    min_network_size: Optional[int] = None
    methods: Optional[PrepMethods] = None


class RoadAccessRestrictions(Parent):
    use_for_warnings: Optional[bool] = None


class ExtStorages(Parent):
    WayCategory: Optional[Dict] = None
    HeavyVehicle: Optional[Union[HeavyVehicle, Dict]] = None
    WaySurfaceType: Optional[Dict] = None
    Tollways: Optional[Dict] = None
    Borders: Optional[Union[Borders, Dict]] = None
    RoadAccessRestrictions: Optional[Union[RoadAccessRestrictions, Dict]] = None
    HereTraffic: Optional[Union[HereTraffic, Dict]] = None
    HillIndex: Optional[Dict] = None
    TrailDifficulty: Optional[Dict] = None
    GreenIndex: Optional[Union[GreenIndex, Dict]] = None
    NoiseIndex: Optional[Dict] = None
    csv: Optional[Dict] = None
    ShadowIndex: Optional[Dict] = None
    Wheelchair: Optional[Union[Wheelchair, Dict]] = None
    OsmId: Optional[Dict] = None


class ProfileEntry(Parent):
    enabled: Optional[bool] = None
    profile: Optional[str] = None
    graph_path: Optional[str] = None
    elevation: Optional[bool] = None
    encoder_options: Optional[EncoderOptions] = None
    ext_storages: Optional[ExtStorages] = None
    elevation_smoothing: Optional[bool] = None
    encoder_flags_size: Optional[int] = None
    instructions: Optional[bool] = None
    optimize: Optional[bool] = None
    traffic: Optional[bool] = None
    maximum_distance: Optional[int] = None
    maximum_distance_dynamic_weights: Optional[int] = None
    maximum_distance_avoid_areas: Optional[int] = None
    maximum_waypoints: Optional[int] = None
    maximum_snapping_radius: Optional[int] = None
    maximum_distance_alternative_routes: Optional[int] = None
    maximum_distance_round_trip_routes: Optional[int] = None
    maximum_speed_lower_bound: Optional[int] = None
    maximum_visited_nodes: Optional[int] = None
    location_index_resolution: Optional[int] = None
    location_index_search_iterations: Optional[int] = None
    force_turn_costs: Optional[bool] = None
    interpolate_bridges_and_tunnels: Optional[bool] = None
    preparation: Optional[Preparation] = None
    execution: Optional[Execution] = None
    gtfs_file: Optional[str] = None


class Profiles(Parent):
    car: Optional[ProfileEntry] = None
    hgv: Optional[ProfileEntry] = None
    bike_regular: Optional[ProfileEntry] = Field(None, alias='bike-regular')
    bike_mountain: Optional[ProfileEntry] = Field(None, alias='bike-mountain')
    bike_road: Optional[ProfileEntry] = Field(None, alias='bike-road')
    bike_electric: Optional[ProfileEntry] = Field(None, alias='bike-electric')
    walking: Optional[ProfileEntry] = None
    hiking: Optional[ProfileEntry] = None
    wheelchair: Optional[ProfileEntry] = None
    public_transport: Optional[ProfileEntry] = Field(None, alias='public-transport')


class Ors(Parent):
    cors: Optional[Cors] = None
    messages: Optional[List[Message]] = None
    endpoints: Optional[Endpoints] = None
    engine: Optional[Engine] = None


class ConditionItem(Parent):
    request_service: Optional[str] = None
    request_profile: Optional[str] = None
    request_preference: Optional[str] = None
    api_format: Optional[str] = None
    api_version: Optional[int] = None
    time_after: Optional[str] = None
    time_before: Optional[str] = None


class Message(Parent):
    active: Optional[bool] = None
    text: Optional[str] = None
    condition: Optional[List[ConditionItem]] = None


class Engine(Parent):
    source_file: Optional[str] = None
    init_threads: Optional[int] = None
    preparation_mode: Optional[bool] = None
    graphs_root_path: Optional[str] = None
    graphs_data_access: Optional[str] = None
    elevation: Optional[Elevation] = None
    profile_default: Optional[ProfileEntry] = None
    profiles: Optional[Profiles] = None


class OrsConfigYML8(Parent):
    server: Optional[Server] = None
    spring: Optional[Spring] = None
    springdoc: Optional[Springdoc] = None
    logging: Optional[Logging] = None
    ors: Optional[Ors] = None
