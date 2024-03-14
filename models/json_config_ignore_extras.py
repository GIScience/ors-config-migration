# generated by datamodel-codegen:
#   filename:  test-config.json
#   timestamp: 2024-03-12T13:17:18+00:00

from __future__ import annotations

from typing import Dict, Optional, Any
from typing import List, Union

from pydantic import BaseModel


class Info(BaseModel):
    base_url: Optional[str] = None
    swagger_documentation_url: Optional[str] = None
    support_mail: Optional[str] = None
    author_tag: Optional[str] = None
    content_licence: Optional[str] = None


class Allowed(BaseModel):
    origins: Optional[List[str]] = None
    headers: Optional[List[str]] = None


class Exposed(BaseModel):
    headers: Optional[List[str]] = None


class Cors(BaseModel):
    allowed: Optional[Allowed] = None
    exposed: Optional[Exposed] = None
    preflight_max_age: Optional[int] = None


class ApiSettings(BaseModel):
    cors: Optional[Cors] = None


class Matrix(BaseModel):
    enabled: Optional[bool] = None
    maximum_routes: Optional[int] = None
    maximum_routes_flexible: Optional[int] = None
    maximum_search_radius: Optional[int] = None
    maximum_visited_nodes: Optional[int] = None
    allow_resolve_locations: Optional[bool] = None
    attribution: Optional[str] = None


class MaximumRangeDistanceItem(BaseModel):
    profiles: Optional[str] = None
    value: Optional[int] = None


class MaximumRangeTimeItem(MaximumRangeDistanceItem):
    pass


class FastIsoDefaultParams(BaseModel):
    enabled: Optional[bool] = None
    threads: Optional[int] = None
    weightings: Optional[str] = None
    maxcellnodes: Optional[int] = None


class Hgv(FastIsoDefaultParams):
    pass


class FastIsoProfiles(BaseModel):
    default_params: Optional[FastIsoDefaultParams] = None
    hgv: Optional[Hgv] = None


class FastIsochrones(BaseModel):
    maximum_range_distance: Optional[List[MaximumRangeDistanceItem]] = None
    maximum_range_time: Optional[List[MaximumRangeTimeItem]] = None
    profiles: Optional[FastIsoProfiles] = None


class PropertyMapping(BaseModel):
    total_pop: Optional[str] = None


class ProviderEntry(BaseModel):
    enabled: Optional[bool] = None
    provider_name: Optional[str] = None
    provider_parameters: Optional[ProviderParameters] = None
    property_mapping: Optional[PropertyMapping] = None
    attribution: Optional[str] = None


class ProviderParameters(BaseModel):
    host: Optional[str] = None
    port: Optional[int] = None
    db_name: Optional[str] = None
    user: Optional[str] = None
    password: Optional[str] = None
    table_name: Optional[str] = None
    geometry_column: Optional[str] = None
    postgis_version: Optional[str] = None

class Isochrones(BaseModel):
    enabled: Optional[bool] = None
    attribution: Optional[str] = None
    maximum_range_distance: Optional[List[MaximumRangeDistanceItem]] = None
    maximum_range_time: Optional[List[MaximumRangeTimeItem]] = None
    fastisochrones: Optional[FastIsochrones] = None
    maximum_intervals: Optional[int] = None
    maximum_locations: Optional[int] = None
    allow_compute_area: Optional[bool] = None
    statistics_providers: Optional[Dict[str, ProviderEntry]] = None


class PrepCH(BaseModel):
    enabled: Optional[bool] = None
    threads: Optional[int] = None
    weightings: Optional[str] = None


class PrepLM(PrepCH):
    landmarks: Optional[int] = None


class PrepCORE(PrepLM):
    lmsets: Optional[str] = None


class PrepMethods(BaseModel):
    lm: Optional[PrepLM] = None
    ch: Optional[PrepCH] = None
    core: Optional[PrepCORE] = None


class Preparation(BaseModel):
    min_network_size: Optional[int] = None
    min_one_way_network_size: Optional[int] = None
    methods: Optional[PrepMethods] = None


class ExecEntry(BaseModel):
    disabling_allowed: Optional[bool] = None
    active_landmarks: Optional[int] = None


class ExecMethods(BaseModel):
    lm: Optional[ExecEntry] = None
    ch: Optional[ExecEntry] = None
    core: Optional[ExecEntry] = None


class Execution(BaseModel):
    methods: Optional[ExecMethods] = None


class Parameters(BaseModel):
    encoder_flags_size: Optional[int] = None
    graphs_root_path: Optional[str] = None
    elevation_provider: Optional[str] = None
    elevation_cache_clear: Optional[bool] = None
    elevation_cache_path: Optional[str] = None
    elevation_smoothing: Optional[bool] = None
    instructions: Optional[bool] = None
    maximum_distance: Optional[int] = None
    maximum_distance_dynamic_weights: Optional[int] = None
    maximum_segment_distance_with_dynamic_weights: Optional[int] = None
    maximum_distance_avoid_areas: Optional[int] = None
    maximum_avoid_polygon_area: Optional[int] = None
    maximum_avoid_polygon_extent: Optional[int] = None
    maximum_distance_round_trip_routes: Optional[int] = None
    maximum_alternative_routes: Optional[int] = None
    maximum_distance_alternative_routes: Optional[int] = None
    maximum_waypoints: Optional[int] = None
    maximum_snapping_radius: Optional[int] = None
    maximum_speed_lower_bound: Optional[int] = None
    preparation: Optional[Preparation] = None
    execution: Optional[Execution] = None
    encoder_options: Optional[str] = None
    elevation: Optional[bool] = None
    ext_storages: Optional[ExtStorages] = None
    traffic: Optional[bool] = None
    interpolate_bridges_and_tunnels: Optional[bool] = None
    maximum_visited_nodes: Optional[int] = None
    gtfs_file: Optional[str] = None


class HeavyVehicle(BaseModel):
    restrictions: Optional[bool] = None


class Borders(BaseModel):
    boundaries: Optional[str] = None
    ids: Optional[str] = None
    openborders: Optional[str] = None


class RoadAccessRestrictions(BaseModel):
    use_for_warnings: Optional[bool] = None


class HereTraffic(BaseModel):
    enabled: Optional[bool] = None
    streets: Optional[str] = None
    ref_pattern: Optional[str] = None
    pattern_15min: Optional[str] = None
    radius: Optional[int] = None
    output_log: Optional[bool] = None
    log_location: Optional[str] = None


class GreenIndex(BaseModel):
    filepath: Optional[str] = None


class Wheelchair(BaseModel):
    KerbsOnCrossings: Optional[str] = None


class ExtStorages(BaseModel):
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


class ProfileEntry(BaseModel):
    profiles: Optional[str] = None
    parameters: Optional[Parameters] = None


# class Profiles(RootModel[Dict[str, Any]]):
    # root = Dict[str, Any]
    # active: Optional[List[str]] = None
    # default_params: Optional[Parameters] = None

class Routing(BaseModel):
    enabled: Optional[bool] = None
    mode: Optional[str] = None
    routing_description: Optional[str] = None
    routing_name: Optional[str] = None
    sources: Optional[List[str]] = None
    init_threads: Optional[int] = None
    attribution: Optional[str] = None
    distance_approximation: Optional[bool] = None
    elevation_preprocessed: Optional[bool] = None
    profiles: Optional[Dict[str, Any]] = None
    storage_format: Optional[str] = None


class Services(BaseModel):
    matrix: Optional[Matrix] = None
    isochrones: Optional[Isochrones] = None
    routing: Optional[Routing] = None


class Logging(BaseModel):
    enabled: Optional[bool] = None
    level_file: Optional[str] = None
    location: Optional[str] = None
    stdout: Optional[bool] = None


class KafkaConsumerItem(BaseModel):
    cluster: Optional[str] = None
    topic: Optional[str] = None
    profile: Optional[str] = None


class Condition(BaseModel):
    request_service: Optional[str] = None
    request_profile: Optional[str] = None
    request_preference: Optional[str] = None
    api_format: Optional[str] = None
    api_version: Optional[int] = None
    time_after: Optional[str] = None
    time_before: Optional[str] = None


class SystemMessageItem(BaseModel):
    active: Optional[bool] = None
    text: Optional[str] = None
    condition: Optional[Condition] = None


class Ors(BaseModel):
    info: Optional[Info] = None
    api_settings: Optional[ApiSettings] = None
    services: Optional[Services] = None
    logging: Optional[Logging] = None
    kafka_test_cluster: Optional[bool] = None
    kafka_consumer: Optional[List[KafkaConsumerItem]] = None
    system_message: Optional[List[SystemMessageItem]] = None


class OrsConfigJSONIgnoreExtras(BaseModel):
    ors: Optional[Ors] = None